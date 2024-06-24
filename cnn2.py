import jieba
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset

jieba.add_word("贴片电容")
jieba.add_word("贴片电阻")
jieba.add_word("贴片电感")
jieba.add_word("MOS管")
jieba.add_word("锂电池充电管理IC")
jieba.add_word("贴片型铝电解电容")
jieba.add_word("直插铝电解电容")
jieba.add_word("钽电容")
jieba.add_word("固态电容")
jieba.add_word("固液混合铝电解电容器")
jieba.add_word("厚膜电阻")
jieba.add_word("稳压二极管")
jieba.add_word("肖特基二极管")
jieba.add_word("通用二极管")
jieba.add_word("静电和浪涌保护(TVS/ESD)")
jieba.add_word("N沟道")
jieba.add_word("P沟道")
jieba.add_word("场效应管(MOSFET)")
jieba.add_word("NPN")
jieba.add_word("PNP")
jieba.add_word("插件电容器")
jieba.add_word("贴片二极管")
jieba.add_word("贴片稳压二极管")
jieba.add_word("贴片MOSFET")

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


# 转换单个样本到模型输入格式
def convert_sample(text, labels):
    # 分词
    words = tokenize_text(text)
    # 标记标签位置
    # 装量数据必须要一致
    label_positions = []
    for label_text, label_name in labels:
        if label_text != "":  # 忽略空标签
            start_idx = text.index(label_text[0])  # 假设标签是连续的文本片段
            end_idx = start_idx + len(label_text)
            label_positions.append((start_idx, end_idx, label2idx[label_name]))
        # else:
        #     # 空标签
        #     label_positions.append((0, 0, label2idx[label_name]))
    print(label_positions)
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
        labels_tensor[start:end, label_idx] = 5  # 假设是多标签情况，如果是单标
    return text_tensor, labels_tensor


# 假设您有一个word到idx的映射（这里只是示例）

def word_to_idx(dataset):
    word2idx = {"<PAD>": 0, "<UNK>": 1}
    for text, labels in dataset:
        for word in jieba.lcut_for_search(text):
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
        self.conv = nn.Conv1d(in_channels=embedding_dim, out_channels=num_filters, kernel_size=3)
        self.fc = nn.Linear(num_filters, num_classes)
        # self.fc = nn.Linear(32 * (32 // 4) * (32 // 4), num_classes)
        print("embedding_dim:", embedding_dim, "num_filters:", num_filters, "num_classes:", num_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.embedding(x)  # (batch_size, seq_length, embedding_dim)
        x = self.dropout(x)
        x = self.fc(x)
        return x


class TextRNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim, n_layers, dropout=0.5):
        super(TextRNN, self).__init__()
        # 嵌入层：将词汇表中的索引转换为词向量
        self.embedding = nn.Embedding(len(word2idx), embed_dim)
        # LSTM层
        self.rnn = nn.LSTM(embed_dim, hidden_dim, num_layers=n_layers,
                           bidirectional=True, dropout=dropout)
        # 全连接层，用于最后的分类
        self.fc = nn.Linear(hidden_dim * 2, output_dim)  # 由于使用了双向LSTM，所以hidden_dim乘以2
        # dropout层，防止过拟合
        self.dropout = nn.Dropout(dropout)

    def forward(self, text):
        # 将词索引通过嵌入层转换为词向量
        x = self.embedding(text)
        embedded = self.dropout(x)
        # 通过LSTM层
        outputs, (hidden, cell) = self.rnn(embedded)
        # 使用最后时间步的隐藏状态进行分类
        hidden = self.dropout(torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=1))
        # 通过全连接层得到最终的分类结果
        return self.fc(hidden.squeeze(0))


# 初始化模型、损失函数和优化器
embedding_dim = len(vocab)
num_filters = len(vocab)
dropout = 0.1
model = TextCNN(embedding_dim, num_filters, num_labels, dropout)
# model = TextRNN(vocab_size=len(vocab), embed_dim=embedding_dim, hidden_dim=64, output_dim=num_labels, n_layers=1,
#                 dropout=dropout)
criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

epoch_losses = []

# 训练模型
def train_model(model, train_loader, criterion, optimizer, num_epochs):
    global loss
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0  # 记录当前epoch的总损失
        for texts, annotations in train_loader:
            optimizer.zero_grad()
            # texts = texts.view(-1, texts.size(-1))  # 调整文本序列的形状
            outputs = model(texts)
            loss = criterion(outputs, annotations)
            loss.backward()
            optimizer.step()
        running_loss += loss.item() * texts.size(0)
        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_losses.append(epoch_loss)
        print(f'Epoch {epoch+1}, Loss: {epoch_loss:.4f}')


num_epochs = 2000
epoch = 2000

def train_model_rnn(model, train_loader, loss_fn, optimizer, num_epochs):
    global epoch
    running_loss = 0.0  # 记录当前epoch的总损失
    for epoch in range(num_epochs):
        model.train()  # 设置模型为训练模式

        for batch_idx, (texts, labels) in enumerate(train_loader):
            optimizer.zero_grad()  # 清零梯度

            # 前向传播
            predictions = model(texts)
            # texts = texts.view(-1, texts.size(-1))  # 调整文本序列的形状
            labels = labels[0]
            # 计算损失
            loss = loss_fn(predictions, labels)

            # 反向传播和优化
            loss.backward()  # 反向传播
            optimizer.step()  # 更新权重

            # epoch_loss += loss.item()
            running_loss += loss.item() * texts.size(0)
            epoch_loss = running_loss / len(train_loader.dataset)
            epoch_losses.append(epoch_loss)
            print(f'Epoch {epoch+1}, Loss: {epoch_loss:.4f}')
        model.eval()  # 设置模型为评估模式
        with torch.no_grad():
            val_loss = 0
            correct = 0
            for texts, labels in dataloader:
                outputs = model(texts)
                _, preds = torch.max(outputs, dim=1)
                newLabel = labels[0]
                loss = loss_fn(outputs, newLabel)

                val_loss += loss.item()
                print(preds.shape)
                print(labels.shape)
                correct += torch.sum(preds == labels)

            val_loss /= len(dataloader.dataset)
            accuracy = correct.double() / len(dataloader.dataset)

            print(f'Epoch [{epoch + 1}/{num_epochs}], Val Loss: {val_loss:.4f}, Accuracy: {accuracy:.4f}')


train_model(model, dataloader, criterion, optimizer, num_epochs)
# train_model_rnn(model, dataloader, criterion, optimizer, num_epochs)

torch.save(model, 'field_extraction_model.pth')

# 保存模型的状态字典
torch.save(model.state_dict(), 'field_extraction_model_state_dict.pth')
import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(1, num_epochs + 1), epoch_losses, label='Training Loss')
plt.title('Training Loss per Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()