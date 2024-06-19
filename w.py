import jieba
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset

from cnn2 import num_labels
from dataset import data

for i in range(len(data)):
    text, annotations_tuple = data[i]
    text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
    annotations_list = list(annotations_tuple)  # 将元组转换为列表
    data[i] = (text, annotations_list)  # 用新的列表替换原来的元组


def tokenize_text(text):
    return list(jieba.cut(text))


# 标签编码：创建标签到索引的映射
label2idx = {
    "Model": 0,
    "Package": 1,
    "Type": 2,
    "Voltage": 3,
    "Cap": 4,
    "Precision": 5,
    "Resistance": 6,
    "Watt": 7,
    "Inductance": 8,
    "Electricity": 9
}


# 转换单个样本到模型输入格式
def convert_sample(text, labels):
    # 分词
    words = tokenize_text(text)

    # 标记标签位置
    label_positions = []
    for label_text, label_name in labels:
        if label_text:  # 忽略空标签
            start_idx = text.index(label_text[0])  # 假设标签是连续的文本片段
            end_idx = start_idx + len(label_text)
            label_positions.append((start_idx, end_idx, label2idx[label_name]))

            # 填充文本到最大长度（如果需要）
    MAX_LENGTH = 100
    padded_words = words[:MAX_LENGTH] + ['<PAD>'] * (MAX_LENGTH - len(words))
    word_indices = [word2idx.get(word, word2idx['<UNK>']) for word in padded_words]  # 假设word2idx是词语到索引的映射

    # 转换为tensor
    text_tensor = torch.tensor(word_indices, dtype=torch.long)
    label_tensor = torch.tensor(label_positions, dtype=torch.long) if label_positions else torch.empty((0, 3),
                                                                                                       dtype=torch.long)

    return text_tensor, label_tensor


# 假设您有一个word到idx的映射（这里只是示例）

def word_to_idx(dataset):
    word2idx = {"<PAD>": 0, "<UNK>": 1}
    for text, labels in dataset:
        for word in text.split():
            if word not in word2idx:
                word2idx[word] = len(word2idx)
    return word2idx


word2idx = word_to_idx(data)

# 转换整个数据集
processed_data = [(convert_sample(text, labels)) for text, labels in data]
print(processed_data)

# 创建一个简单的Dataset类
class MyDataset(Dataset):
    def __init__(self, processed_data):
        self.processed_data = processed_data

    def __len__(self):
        return len(self.processed_data)

    def __getitem__(self, idx):
        return self.processed_data[idx]

    # 创建DataLoader


dataset = MyDataset(processed_data)
dataloader = DataLoader(dataset, batch_size=1, shuffle=False)




# 定义CNN模型
class TextCNN(nn.Module):
    def __init__(self, embedding_dim, num_filters, num_classes, dropout):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(len(vocab), embedding_dim)
        self.conv = nn.Conv1d(in_channels=embedding_dim, out_channels=num_filters, kernel_size=3)
        self.fc = nn.Linear(num_filters, num_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.embedding(x)  # (batch_size, seq_length, embedding_dim)
        x = x.permute(0, 2, 1)  # (batch_size, embedding_dim, seq_length)
        x = self.conv(x)  # (batch_size, num_filters, seq_length - kernel_size + 1)
        x = torch.max(x, 1)[0]  # (batch_size, num_filters)
        x = self.dropout(x)
        x = self.fc(x)
        return x


# 初始化模型、损失函数和优化器
embedding_dim = 50
num_filters = 100
dropout = 0.5
model = TextCNN(embedding_dim, num_filters, num_labels, dropout)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# 训练模型
def train_model(model, train_loader, criterion, optimizer, num_epochs):
    global loss
    model.train()
    for epoch in range(num_epochs):
        for texts, annotations in train_loader:
            optimizer.zero_grad()
            texts = texts.view(-1, texts.size(-1))  # 调整文本序列的形状
            outputs = model(texts)
            loss = criterion(outputs, annotations)
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}')


num_epochs = 10
train_model(model, dataloader, criterion, optimizer, num_epochs)
