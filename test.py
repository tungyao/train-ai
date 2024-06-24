import jieba
import torch
from torch import nn, optim
jieba.add_word("贴片电容")
jieba.add_word("贴片电阻")
jieba.add_word("贴片电感")
jieba.add_word("电容值")
jieba.add_word("电压")
jieba.add_word("NPN")
jieba.add_word("PNP")
jieba.add_word("N沟道")
jieba.add_word("P沟道")
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


class TextCNN(nn.Module):
    def __init__(self, embedding_dim, num_filters, num_classes, dropout):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(len(word2idx), embedding_dim)
        self.conv = nn.Conv1d(in_channels=embedding_dim, out_channels=num_filters, kernel_size=3)
        self.fc = nn.Linear(num_filters, num_classes)
        # self.fc = nn.Linear(32 * (input_size // 4) * (input_size // 4), num_classes)
        print("embedding_dim:", embedding_dim, "num_filters:", num_filters, "num_classes:", num_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.embedding(x)  # (batch_size, seq_length, embedding_dim)
        x = self.dropout(x)
        x = self.fc(x)
        return x




def tokenize_text(text):
    return list(jieba.lcut_for_search(text))


from dataset import data

for i in range(len(data)):
    text, annotations_tuple = data[i]
    text = text.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
    annotations_list = list(annotations_tuple)  # 将元组转换为列表
    data[i] = (text, annotations_list)  # 用新的列表替换原来的元组

vocab = set(value for _, annotations in data for value, _ in annotations)
vocab = sorted(vocab)  # 排序以保持索引一致


def word_to_idx(dataset):
    word2idx = {"<PAD>": 0, "<UNK>": 1}
    for text, labels in dataset:
        for word in jieba.lcut(text):
            if word not in word2idx:
                word2idx[word] = len(word2idx)
    return word2idx


word2idx = word_to_idx(data)


def predict(model, text):
    words = tokenize_text(text)
    MAX_LENGTH = len(vocab)

    padded_words = words[:MAX_LENGTH] + ['<PAD>'] * (MAX_LENGTH - len(words))
    word_indices = [word2idx.get(word, word2idx['<UNK>']) for word in padded_words]  # 假设word2idx是词语到索引的映射

    # print(words , word_indices , label_positions)
    # 转换为tensor
    input_ids = torch.tensor(word_indices, dtype=torch.long)

    with torch.no_grad():
        tag_scores = model(input_ids)

    print(tag_scores)
    _, predicted_labels = torch.max(tag_scores,dim=1)
    predicted_labels = predicted_labels.squeeze().tolist()
    labels = [list(label2idx.keys())[label_id] for label_id in predicted_labels]
    return list(zip(words, labels))

model = TextCNN(158, 158, 10, 0.5)
model.load_state_dict(torch.load("field_extraction_model_state_dict.pth"))
model.eval()

text = "原装正品0603贴片电容25V 100NF ±10% X7R CL10B104KA8NNNC 50只"
predictions = predict(model, text)
print(predictions)
