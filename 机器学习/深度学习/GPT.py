import torch
import torch.nn as nn
import torch.optim as optim
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# GPT 解码器的自注意力（Masked Self-Attention）
class MaskedSelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(MaskedSelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads

        assert self.head_dim * heads == embed_size, "Embed size must be divisible by heads"

        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, embed_size)
        self.value = nn.Linear(embed_size, embed_size)
        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, x, mask):
        batch_size, seq_length, embed_size = x.shape

        Q = self.query(x).view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2)
        K = self.key(x).view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2)
        V = self.value(x).view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2)

        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.head_dim ** 0.5)

        # 添加 Mask，确保不能“偷看”未来的词
        scores = scores.masked_fill(mask == 0, float('-inf'))
        attention = torch.softmax(scores, dim=-1)
        out = torch.matmul(attention, V)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_length, self.embed_size)
        return self.fc_out(out)

# GPT 解码器块（Transformer Decoder Block）
class GPTDecoderBlock(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
        super(GPTDecoderBlock, self).__init__()
        self.attention = MaskedSelfAttention(embed_size, heads)
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)
        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, forward_expansion * embed_size),
            nn.ReLU(),
            nn.Linear(forward_expansion * embed_size, embed_size),
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        attn = self.attention(x, mask)
        x = self.norm1(attn + x)
        forward = self.feed_forward(x)
        out = self.norm2(forward + x)
        return out

# GPT 模型
class GPT(nn.Module):
    def __init__(self, embed_size, num_layers, heads, dropout, forward_expansion, vocab_size):
        super(GPT, self).__init__()
        self.embed_size = embed_size
        self.word_embedding = nn.Embedding(vocab_size, embed_size)
        self.position_embedding = nn.Embedding(100, embed_size)          # 假设最多 100 词
        self.layers = nn.ModuleList([
            GPTDecoderBlock(embed_size, heads, dropout, forward_expansion)
            for _ in range(num_layers)
        ])
        self.fc_out = nn.Linear(embed_size, vocab_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        positions = torch.arange(0, x.shape[1]).expand(x.shape[0], x.shape[1]).to(x.device)
        x = self.dropout(self.word_embedding(x) + self.position_embedding(positions))
        for layer in self.layers:
            x = layer(x, mask)
        return self.fc_out(x)

# 测试 GPT
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vocab_size = 5000                                          # 假设有 5000 个单词
model = GPT(embed_size=128, num_layers=6, heads=8, dropout=0.1, forward_expansion=4, vocab_size=vocab_size).to(device)

# 生成一个 32 句子（batch），每个句子 10 词
x = torch.randint(0, vocab_size, (32, 10)).to(device)      # 随机输入（词索引）
mask = torch.tril(torch.ones((10, 10))).to(device)         # 因果 Mask（保证每个词只能看到自己之前的词）
out = model(x, mask)
print("GPT 输出形状:", out.shape)                           # (32, 10, vocab_size)


------------------------------------------------------------------------------------------------------------------------------------------------------------


# 加载预训练模型 & 分词器（调库实现）
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# 输入文本
input_text = "The future of AI is"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# 生成文本
output = model.generate(input_ids, max_length=50, temperature=1.0, top_k=100)

# 解码输出
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("\nGenerated Text:\n", generated_text)




