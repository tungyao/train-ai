import os

import jieba
from dataset import data

jieba.add_word("贴片电容")
jieba.add_word("贴片电阻")
jieba.add_word("贴片电感")
jieba.add_word("电容值")
jieba.add_word("电压")
jieba.add_word("NPN")
jieba.add_word("PNP")
jieba.add_word("N沟道")
jieba.add_word("P沟道")

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer
from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pad_packed_sequence

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')


class FieldExtractionDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer
        self.label_map = {"O": 0, "B-Model": 1, "I-Model": 2, "B-Package": 3, "I-Package": 4,
                          "B-Type": 5, "I-Type": 6, "B-Voltage": 7, "I-Voltage": 8,
                          "B-Cap": 9, "I-Cap": 10, "B-Precision": 11, "I-Precision": 12,
                          "B-Resistance": 13, "I-Resistance": 14, "B-Watt": 15, "I-Watt": 16,
                          "B-Inductance": 17, "I-Inductance": 18, "B-Electricity": 19, "I-Electricity": 20}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text, annotations = self.data[idx]

        # 移除空格
        text = text.replace(" ", "").replace("\n", "").replace("\r", "").replace("\t", "").replace(":", "").replace("：",
                                                                                                                    "").replace(
            '±', "")
        tokens = jieba.lcut(text)
        labels = ["O"] * len(tokens)
        for annotation in annotations:
            value, label = annotation
            value_tokens = tokenizer.tokenize(value)
            for i in range(len(tokens) - len(value_tokens) + 1):
                if tokens[i:i + len(value_tokens)] == value_tokens:
                    labels[i] = f"B-{label}"
                    for j in range(1, len(value_tokens)):
                        labels[i + j] = f"I-{label}"
                    break

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        label_ids = [self.label_map[label] for label in labels]

        return torch.tensor(input_ids), torch.tensor(label_ids)


dataset = FieldExtractionDataset(data, tokenizer)


def collate_fn(batch):
    (input_ids, label_ids) = zip(*batch)
    input_ids_padded = pad_sequence(input_ids, batch_first=True, padding_value=0)
    label_ids_padded = pad_sequence(label_ids, batch_first=True, padding_value=0)
    return input_ids_padded, label_ids_padded


dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

import torch.nn as nn


class BiLSTMModel(nn.Module):
    def __init__(self, vocab_size, tagset_size, embedding_dim=128, hidden_dim=64):
        super(BiLSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim // 2, num_layers=1, bidirectional=True)
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)

    def forward(self, sentence):
        embeds = self.embedding(sentence)
        lstm_out, _ = self.lstm(embeds)
        tag_space = self.hidden2tag(lstm_out)
        tag_scores = torch.log_softmax(tag_space, dim=2)
        return tag_scores


vocab_size = len(tokenizer.vocab)
tagset_size = len(dataset.label_map)
model = BiLSTMModel(vocab_size, tagset_size)

import torch.optim as optim

loss_function = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(10):  # 训练10个epoch
    for inputs, labels in dataloader:
        model.zero_grad()
        tag_scores = model(inputs)
        tag_scores = tag_scores.view(-1, tagset_size)
        labels = labels.view(-1)
        loss = loss_function(tag_scores, labels)
        loss.backward()
        optimizer.step()

torch.save(model, 'field_extraction_model.pth')

# 保存模型的状态字典
torch.save(model.state_dict(), 'field_extraction_model_state_dict.pth')


def predict(model, tokenizer, text):
    tokens = tokenizer.tokenize(text)
    input_ids = torch.tensor(tokenizer.convert_tokens_to_ids(tokens)).unsqueeze(0)
    with torch.no_grad():
        tag_scores = model(input_ids)
    _, predicted_labels = torch.max(tag_scores, dim=2)
    predicted_labels = predicted_labels.squeeze().tolist()
    labels = [list(dataset.label_map.keys())[label_id] for label_id in predicted_labels]
    return list(zip(tokens, labels))


text = "原装正品0603贴片电容25V 100NF ±10% X7R CL10B104KA8NNNC 50只"
predictions = predict(model, tokenizer, text)
print(predictions)
