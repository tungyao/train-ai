import jieba

# 添加自定义词汇到 jieba 的词典中
jieba.add_word("贴片电容")
jieba.add_word("电容值")
jieba.add_word("电压")

text = "原装正品0603贴片电容25V 100NF ±10% X7R CL10B104KA8NNNC 50只"
text = text.replace(" ", "")
# 使用 jieba 分词
tokens = jieba.lcut(text)
print(tokens)