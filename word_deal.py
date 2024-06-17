import os

import jieba
jieba.add_word("贴片电容")
jieba.add_word("贴片电阻")
jieba.add_word("贴片电感")
jieba.add_word("电容值")
jieba.add_word("电压")
jieba.add_word("MOS管")
data = [
    ("原装正品0603贴片电容25V 100NF ±10% X7R CL10B104KA8NNNC 50只",
     [("CL10B104KA8NNNC", "型号"),
      ("0603", "封装"),
      ("贴片电容", "类型"),
      ("25V", "电压"),
      ("100NF", "电容值"),
      ("10%", "精度"),
      ("", "电阻值"),
      ("", "功率"),
      ("", "电感值"),
      ("", "电流"),

      ]),
    ("原装正品0603贴片电阻 1K 标字102 1/10W 精度5% （200只）",
     [("", "型号"),
      ("0603", "封装"),
      ("贴片电阻", "类型"),
      ("", "电压"),
      ("", "电容值"),
      ("5%", "精度"),
      ("1K", "电阻值"),
      ("1/10W", "功率"),
      ("", "电感值"),
      ("", "电流"),

      ]),
    ("原装正品 0603贴片电阻 22R 22欧 1/10W 精度±1% （50只）",
     [("", "型号"),
      ("0603", "封装"),
      ("贴片电阻", "类型"),
      ("", "电压"),
      ("", "电容值"),
      ("1%", "精度"),
      ("22R", "电阻值"),
      ("1/10W", "功率"),
      ("", "电感值"),
      ("", "电流"),

      ]),
    ("0603贴片电感 2.2UH ±10% EBLS1608-2R2K (50只）",
     [("EBLS1608-2R2K", "型号"),
      ("0603", "封装"),
      ("贴片电感", "类型"),
      ("", "电压"),
      ("", "电容值"),
      ("10%", "精度"),
      ("", "电阻值"),
      ("", "功率"),
      ("2.2UH", "电感值"),
      ("", "电流"),

      ]),
    ("贴片 AO3401 SOT-23 MOS管/三极管/场效应管 2.8A（20只）",
     [("AO3401", "型号"),
      ("SOT-23", "封装"),
      ("MOS管", "类型"),
      ("", "电压"),
      ("", "电容值"),
      ("", "精度"),
      ("", "电阻值"),
      ("", "功率"),
      ("", "电感值"),
      ("2.8A", "电流"),

      ]),
    ("原装正品 SGM4056-6.8YTDE8G/TR 丝印SG7 TDFN8 锂电池充电管理IC",
     [("SGM4056-6.8YTDE8G/TR", "型号"),
      ("TDFN8", "封装"),
      ("锂电池充电管理IC", "类型"),
      ("", "电压"),
      ("", "电容值"),
      ("", "精度"),
      ("", "电阻值"),
      ("", "功率"),
      ("", "电感值"),
      ("", "电流"),

      ])
]

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer
from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pad_packed_sequence

tokenizer = AutoTokenizer.from_pretrained('bert-base-english')



class FieldExtractionDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.data = data
        self.tokenizer = tokenizer
        self.label_map = {"O": 0, "B-型号": 1, "I-型号": 2, "B-封装": 3, "I-封装": 4,
                          "B-类型": 5, "I-类型": 6, "B-电压": 7, "I-电压": 8,
                          "B-电容值": 9, "I-电容值": 10, "B-精度": 11, "I-精度": 12,
                          "B-电阻值": 13, "I-电阻值": 14, "B-功率": 15, "I-功率": 16,
                          "B-电感值": 17, "I-电感值": 18, "B-电流": 19, "I-电流": 20}
        # self.label_map = {
        #     "0":0,
        #     "型号":1,
        #     "封装":2,
        #     "类型":3,
        #     "电压":4,
        #     "电容值":5,
        #     "精度":6,
        #     "电阻值":7,
        #     "功率":8,
        #     "电感值":9,
        #     "电流":10,
        # }

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text, annotations = self.data[idx]

        # 移除空格
        text = text.replace(" ", "")

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
