import torch
from transformers import BertTokenizer
import torch.nn as nn

# 加载预训练的BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')


# 定义模型结构（必须和训练时一致）
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


# 加载数据集中的label map（必须和训练时一致）
label_map = {"O": 0, "B-型号": 1, "I-型号": 2, "B-封装": 3, "I-封装": 4,
             "B-类型": 5, "I-类型": 6, "B-电压": 7, "I-电压": 8,
             "B-电容值": 9, "I-电容值": 10, "B-精度": 11, "I-精度": 12,
             "B-电阻值": 13, "I-电阻值": 14, "B-功率": 15, "I-功率": 16,
             "B-电感值": 17, "I-电感值": 18, "B-电流": 19, "I-电流": 20}

# 加载模型
vocab_size = len(tokenizer.vocab)
tagset_size = len(label_map)
model = BiLSTMModel(vocab_size, tagset_size)

# 加载模型的状态字典
model.load_state_dict(torch.load('field_extraction_model_state_dict.pth'))
model.eval()


# 定义预测函数
def predict(model, tokenizer, text):
    tokens = tokenizer.tokenize(text)
    input_ids = torch.tensor(tokenizer.convert_tokens_to_ids(tokens)).unsqueeze(0)
    with torch.no_grad():
        tag_scores = model(input_ids)
    _, predicted_labels = torch.max(tag_scores, dim=2)
    predicted_labels = predicted_labels.squeeze().tolist()
    labels = [list(label_map.keys())[label_id] for label_id in predicted_labels]
    return list(zip(tokens, labels))


# 使用模型进行预测
text = "原装正品0603贴片电容25V 100NF ±10% X7R CL10B104KA8NNNC 50只"
predictions = predict(model, tokenizer, text)
print(predictions)
