import torch
import torch.nn as nn
import torch.optim as optim

# 自注意力机制（Self-Attention）
class SelfAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size                        # 嵌入大小
        self.heads = heads                                  # 头的数量
        self.head_dim = embed_size // heads                 # 给每个头分配一定任务(嵌入数)
    # assert:断言，确保条件一定是对的
        assert self.head_dim * heads == embed_size, "维度总量不能变嗷！"

        self.query = nn.Linear(embed_size, embed_size)      # 询问信息（部分token）
        self.key = nn.Linear(embed_size, embed_size)        # 查找信息（全token）
        self.value = nn.Linear(embed_size, embed_size)      # 提取信息（全token）
        self.fc_out = nn.Linear(embed_size, embed_size)     # 计算最终输出

    def forward(self, x):
        batch_size, seq_length, embed_size = x.shape

        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.head_dim ** 0.5)      # 计算Q对每个K的匹配度
        attention = torch.softmax(scores, dim=-1)                                   # 数据归一化，得到各个概率

        out = torch.matmul(attention, V)                    # 将概率带回，计算V，得到最终答案
        return self.fc_out(out)                             # 将形状调回，继续之后计算

# tansformer 编码器
class TransformerBlock(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
# embed_size：输入数据的维度（特征数）
# heads：注意力头的数量（用于多头自注意力）
# dropout：防止过拟合的 Dropout 概率
# forward_expansion：前馈神经网络（FFN）的扩展比例（一般设为4,表示FFN维度是4 * embed_size）
        
        super(TransformerBlock, self).__init__()
        self.attention = SelfAttention(embed_size, heads)               # 自注意力层
        self.norm1 = nn.LayerNorm(embed_size)                           # 归一化层，稳定数据
        self.norm2 = nn.LayerNorm(embed_size)                           # 归一化层，稳定数据
        self.feed_forward = nn.Sequential(                              # 前馈神经网络
            nn.Linear(embed_size, forward_expansion * embed_size),      # 维度扩展
            nn.ReLU(),                                                  # 激活函数
            nn.Linear(forward_expansion * embed_size, embed_size),      # 收缩维度，压回原大小
        )
        self.dropout = nn.Dropout(dropout)                              # 随机丢弃一部分神经元,防止模型过度依赖

    def forward(self, x):
        attn = self.attention(x)
        x = self.norm1(attn + x)                                       # 直接叠啦，类似残差
        forward = self.feed_forward(x)
        out = self.norm2(forward + x)
        return out

# 构建 Transformer
class Transformer(nn.Module):
    def __init__(self, embed_size, num_layers, heads, dropout, forward_expansion):
        super(Transformer, self).__init__()
        self.layers = nn.ModuleList([
            TransformerBlock(embed_size, heads, dropout, forward_expansion)
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(embed_size)

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return self.norm(x)

# 测试 Transformer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Transformer(embed_size=128, num_layers=6, heads=8, dropout=0.1, forward_expansion=4).to(device)

x = torch.rand(32, 10, 128).to(device)          # batch=32, 序列长度=10, 维度=128
out = model(x)
print("Transformer 输出形状:", out.shape)        # 预期 (32, 10, 128)

-----------------------------------------------------------------------------------------------------------------

# 完整版,加入解码器（Decoder），位置编码，mask屏蔽

class SelfAttention(nn.Module):                                            # 自注意力机制（Self-Attention）
    def __init__(self, embed_size, heads):
        super(SelfAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads

        assert self.head_dim * heads == embed_size, "Embed size must be divisible by heads"

        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, embed_size)
        self.value = nn.Linear(embed_size, embed_size)
        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, x, mask=None):
        batch_size, seq_length, embed_size = x.shape

        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.head_dim ** 0.5)

        if mask is not None:                                           # 加入mask
            scores = scores.masked_fill(mask == 0, float('-inf'))      # 对填充（padding）部分屏蔽，不仅防止模型训练时关注到无意义的填充部分，还可以防止生成类模型作弊，偷窥“未来”

        attention = torch.softmax(scores, dim=-1)
        out = torch.matmul(attention, V)
        return self.fc_out(out)

# Transformer 编码器块（Encoder Block）
class TransformerBlock(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
        super(TransformerBlock, self).__init__()
        self.attention = SelfAttention(embed_size, heads)
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

# Transformer 编码器（Encoder）
class Encoder(nn.Module):
    def __init__(self, embed_size, num_layers, heads, dropout, forward_expansion, vocab_size, max_length):
        # embed_size：词维度，原数据x的只有（批，句，词），实际只是表示每批有多少句子，我们将在这里给每个词（token）打入自己的embed_size（词向量）词嵌入，让模型开始关联各个词token的att
        # num_layers：轮数
        # heads：头数
        # dropout：dropout力度
        # forward_expansion:FF层的扩展比例
        # vocab_size：词典大小
        # max_length：句子长度限制
        super(Encoder, self).__init__()
        self.embed_size = embed_size
        self.word_embedding = nn.Embedding(vocab_size, embed_size)                                        # 词嵌入，启动！
        self.position_embedding = nn.Embedding(max_length, embed_size)                                    # 位置编码，启动！
        self.layers = nn.ModuleList([
            TransformerBlock(embed_size, heads, dropout, forward_expansion)
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(embed_size)

    def forward(self, x, mask):
        batch_size, seq_length = x.shape
        positions = torch.arange(0, seq_length).expand(batch_size, seq_length).to(x.device)               # 先构建位置序列0 ~ seq_length 再expand延展成(batch_size, seq_length)嗯，每一句话都是一样的序列，以句为大单位
        
        out = self.word_embedding(x) + self.position_embedding(positions)                                 # Transformer 不像 RNN、CNN 那样天然有“顺序感”，它是一个全连接结构，不能知道词语在句子里的位置。
                                                                                                          # 所以我们将词id映射为词向量（词嵌入）再为每个词添加位置信息（位置嵌入），给每个词加上“它在句子中的位置”
                                                                                                          # 否则，模型只知道词本身，不知道它排第几个，结果就会很怪，比如：“你今天真帅”和“真你帅今天”在模型眼里可能是一样的       


        for layer in self.layers:
            out = layer(out, mask)

        return self.norm(out)

# Transformer 解码器块（Decoder Block）
class DecoderBlock(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
        super(DecoderBlock, self).__init__()
        self.attention = SelfAttention(embed_size, heads)
        self.norm1 = nn.LayerNorm(embed_size)
        self.transformer_block = TransformerBlock(embed_size, heads, dropout, forward_expansion)
        self.norm2 = nn.LayerNorm(embed_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, enc_out, src_mask, tgt_mask):
        attn = self.attention(x, tgt_mask)
        query = self.norm1(attn + x)
        out = self.transformer_block(query, src_mask)
        return out                                                            # 看起来和编码器没什么区别

# Transformer 解码器（Decoder）
class Decoder(nn.Module):
    def __init__(self, embed_size, num_layers, heads, dropout, forward_expansion, vocab_size, max_length):        
        super(Decoder, self).__init__()
        self.embed_size = embed_size
        self.word_embedding = nn.Embedding(vocab_size, embed_size)            
        self.position_embedding = nn.Embedding(max_length, embed_size)      
        self.layers = nn.ModuleList([                                            
            DecoderBlock(embed_size, heads, dropout, forward_expansion)
            for _ in range(num_layers)
        ])
        self.fc_out = nn.Linear(embed_size, vocab_size)
        self.norm = nn.LayerNorm(embed_size)                    

    def forward(self, x, enc_out, src_mask, tgt_mask):
        # enc_out：编码器的输出
        # src_mask：源语言掩码，用于屏蔽源句中的填充位（padding），防止模型在注意力计算时“关注无意义的 pad token”。
        # tgt_mask：目标语言掩码，这是“未来信息屏蔽”机制，防止解码器看到它“还没生成的词”
        batch_size, seq_length = x.shape                                       
        positions = torch.arange(0, seq_length).expand(batch_size, seq_length).to(x.device)               

        x = self.word_embedding(x) + self.position_embedding(positions)                                    
        for layer in self.layers:
            x = layer(x, enc_out, src_mask, tgt_mask)                                                       

        return self.fc_out(self.norm(x))

# 完整 Transformer 模型（Encoder + Decoder）
class Transformer(nn.Module):
    def __init__(self, embed_size, num_layers, heads, dropout, forward_expansion, src_vocab_size, tgt_vocab_size, max_length):
        super(Transformer, self).__init__()
        self.encoder = Encoder(embed_size, num_layers, heads, dropout, forward_expansion, src_vocab_size, max_length)
        self.decoder = Decoder(embed_size, num_layers, heads, dropout, forward_expansion, tgt_vocab_size, max_length)

    def forward(self, src, tgt, src_mask, tgt_mask):
        enc_out = self.encoder(src, src_mask)
        out = self.decoder(tgt, enc_out, src_mask, tgt_mask)
        return out

# 测试 Transformer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Transformer(
    embed_size=128, num_layers=6, heads=8, dropout=0.1, forward_expansion=4,
    src_vocab_size=5000, tgt_vocab_size=5000, max_length=100
).to(device)

src = torch.randint(0, 5000, (32, 10)).to(device)          # 32 个句子，每个句子 10 个单词（源语言）
tgt = torch.randint(0, 5000, (32, 10)).to(device)          # 目标语言输入
src_mask = None                                            # 这里为了简化，不使用 mask
tgt_mask = None                                            # 这里为了简化，不使用 mask

out = model(src, tgt, src_mask, tgt_mask)
print("Transformer 输出形状:", out.shape)  # 预期 (32, 10, 5000)
