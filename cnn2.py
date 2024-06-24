import jieba
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset
jieba.add_word("贴片电容")
jieba.add_word("贴片电阻")
jieba.add_word("贴片电感")
jieba.add_word("电容值")
jieba.add_word("电压")
jieba.add_word("NPN")
jieba.add_word("PNP")
jieba.add_word("N沟道")
jieba.add_word("P沟道")

from dataset import data

for i in range(len(data)):
    text, annotations_tuple = data[i]
    text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
    annotations_list = list(annotations_tuple)  # 将元组转换为列表
    data[i] = (text, annotations_list)  # 用新的列表替换原来的元组


def tokenize_text(text):
    return list(jieba.lcut_for_search(text))


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

num_labels = len(label2idx)
vocab = set(value for _, annotations in data for value, _ in annotations)
vocab = sorted(vocab)  # 排序以保持索引一致
print(vocab)


# 转换单个样本到模型输入格式
def convert_sample(text, labels):
    # 分词
    words = tokenize_text(text)
    print(words)
    # 标记标签位置
    # 装量数据必须要一致
    label_positions = []
    for label_text, label_name in labels:
        if label_text:  # 忽略空标签
            start_idx = text.index(label_text[0])  # 假设标签是连续的文本片段
            end_idx = start_idx + len(label_text)
            label_positions.append((start_idx, end_idx, label2idx[label_name]))
        else:
            # 空标签
            label_positions.append((0, 0, label2idx[label_name]))
    MAX_LENGTH = len(vocab)
    padded_words = words[:MAX_LENGTH] + ['<PAD>'] * (MAX_LENGTH - len(words))
    word_indices = [word2idx.get(word, word2idx['<UNK>']) for word in padded_words]  # 假设word2idx是词语到索引的映射

    # print(words , word_indices , label_positions)
    # 转换为tensor
    text_tensor = torch.tensor(word_indices, dtype=torch.long)

    # labels_tensor = torch.tensor( num_labels, dtype=torch.long)
    # label_tensor = torch.tensor(label_positions, dtype=torch.long)
    labels_tensor = torch.zeros(MAX_LENGTH, num_labels, dtype=torch.float)
    for start, end, label_idx in label_positions:
        labels_tensor[start:end, label_idx] = 1  # 假设是多标签情况，如果是单标
    return text_tensor, labels_tensor


# 假设您有一个word到idx的映射（这里只是示例）

def word_to_idx(dataset):
    word2idx = {"<PAD>": 0, "<UNK>": 1}
    for text, labels in dataset:
        for word in jieba.lcut(text):
            if word not in word2idx:
                word2idx[word] = len(word2idx)
    return word2idx


word2idx = word_to_idx(data)

# 转换整个数据集
processed_data = [(convert_sample(text, labels)) for text, labels in data]


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
dataloader = DataLoader(dataset, batch_size=158, shuffle=True)


# 定义CNN模型
class TextCNN(nn.Module):
    def __init__(self, embedding_dim, num_filters, num_classes, dropout):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(len(word2idx), embedding_dim)
        self.conv = nn.ConvTranspose1d(in_channels=embedding_dim, out_channels=num_filters, kernel_size=3)
        self.fc = nn.Linear(num_filters, num_classes)
        # self.fc = nn.Linear(32 * (32 // 4) * (32 // 4), num_classes)
        print("embedding_dim:", embedding_dim, "num_filters:", num_filters, "num_classes:", num_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.embedding(x)  # (batch_size, seq_length, embedding_dim)
        x = self.dropout(x)
        x = self.fc(x)
        return x


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

# 初始化模型、损失函数和优化器
embedding_dim = len(vocab)
num_filters = len(vocab)
dropout = 0.1
model = TextCNN(embedding_dim, num_filters, num_labels, dropout)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# 训练模型
def train_model(model, train_loader, criterion, optimizer, num_epochs):
    global loss
    model.train()
    for epoch in range(num_epochs):
        for texts, annotations in train_loader:
            optimizer.zero_grad()
            # texts = texts.view(-1, texts.size(-1))  # 调整文本序列的形状
            outputs = model(texts)
            loss = criterion(outputs, annotations)
            loss.backward()
            optimizer.step()
        print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}')


num_epochs = 2000
train_model(model, dataloader, criterion, optimizer, num_epochs)

torch.save(model, 'field_extraction_model.pth')

# 保存模型的状态字典
torch.save(model.state_dict(), 'field_extraction_model_state_dict.pth')
