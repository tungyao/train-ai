import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer
from dataset import data as  DATA

# 定义标签映射
label_map = {
    "Model": 0,
    "Package": 1,
    "Type": 2,
    "Voltage": 3,
    "Cap": 4,
    "Precision": 5,
    "Resistance": 6,
    "Watt": 7,
    "Inductance": 8,
    "Electricity": 9,
    "O": 10  # 'O'表示无标签
}

# 加载预训练的BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')


class CustomDataset(Dataset):
    def __init__(self, data, tokenizer, label_map , max_length):
        self.data = data
        self.tokenizer = tokenizer
        self.label_map = label_map
        self.max_length = max_length
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text, labels = self.data[idx]
        tokens = tokenizer.tokenize(text)
        token_labels = ['O'] * len(tokens)
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_length,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        for label, label_type in labels:
            if label:  # 如果label不为空
                label_tokens = tokenizer.tokenize(label)
                for i, token in enumerate(tokens):
                    if token == label_tokens[0] and tokens[i:i + len(label_tokens)] == label_tokens:
                        token_labels[i:i + len(label_tokens)] = [label_type] * len(label_tokens)

        # input_ids = tokenizer.convert_tokens_to_ids(tokens)
        input_ids = encoding['input_ids'].flatten()
        label_ids = [self.label_map[label] for label in token_labels]

        return {
            'input_ids': torch.tensor(input_ids),
            'labels': torch.tensor(label_ids)
        }


# 创建数据集
dataset = CustomDataset(DATA, tokenizer, label_map)


def collate_fn(batch):
    # 将批次中的序列填充到相同的长度
    input_ids = [item['input_ids'] for item in batch]
    attention_masks = [item['attention_mask'] for item in batch]
    labels = [item['labels'] for item in batch]

    # 使用torch.stack来堆叠张量
    input_ids = torch.stack(input_ids)
    attention_masks = torch.stack(attention_masks)
    labels = torch.stack(labels)

    return {
        'input_ids': input_ids,
        'attention_mask': attention_masks,
        'labels': labels
    }
# print(dataset)
# def collate_fn(batch):
#     (input_ids, label_ids) = zip(*batch)
#     input_ids_padded = pad_sequence(input_ids, batch_first=True, padding_value=0)
#     label_ids_padded = pad_sequence(label_ids, batch_first=True, padding_value=0)
#     return input_ids_padded, label_ids_padded
#
#
# dataloader = DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)

dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

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
