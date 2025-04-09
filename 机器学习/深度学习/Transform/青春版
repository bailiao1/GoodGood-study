import torch
import torch.nn as nn
from RoPE import apply_rotary_pos_emb
import torch.nn.functional as F


# RMSNorm 修正
class RMSNorm(nn.Module):
    def __init__(self, embed_size, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.scale = nn.Parameter(torch.ones(embed_size))

    def forward(self, x):
        rms = torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True) + self.eps)
        return self.scale * x / rms

# SwiGLU 修正（无偏置 + SiLU）
class SwiGLU(nn.Module):
    def __init__(self, embed_size, expansion_factor=4):
        super().__init__()
        hidden_dim = embed_size * expansion_factor
        self.fc1 = nn.Linear(embed_size, hidden_dim, bias=False)
        self.fc2 = nn.Linear(hidden_dim, embed_size, bias=False)
        self.gate = nn.Linear(embed_size, hidden_dim, bias=False)

    def forward(self, x):
        return self.fc2(F.silu(self.fc1(x)) * self.gate(x))

# 带因果 Mask 的注意力机制
class Attention(nn.Module):
    def __init__(self, embed_size, heads):
        super().__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads
        self.qkv = nn.Linear(embed_size, embed_size * 3, bias=False)
        self.fc_out = nn.Linear(embed_size, embed_size, bias=False)

    def forward(self, x, position_ids, mask=None):
        batch_size, seq_length, _ = x.shape
        qkv = self.qkv(x).chunk(3, dim=-1)
        Q, K, V = [t.view(batch_size, seq_length, self.heads, self.head_dim).transpose(1, 2) for t in qkv]

        Q, K = apply_rotary_pos_emb(Q, position_ids), apply_rotary_pos_emb(K, position_ids)
        scores = torch.einsum("bhqd, bhkd -> bhqk", Q, K) / (self.head_dim ** 0.5)

        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))

        attention = torch.softmax(scores, dim=-1)
        out = torch.matmul(attention, V).transpose(1, 2).contiguous().view(batch_size, seq_length, self.embed_size)
        return self.fc_out(out)

# Transformer 解码块（带因果 Mask）
class DecoderBlock(nn.Module):
    def __init__(self, embed_size, heads):
        super().__init__()
        self.attention = Attention(embed_size, heads)
        self.norm1 = RMSNorm(embed_size)
        self.ffn = SwiGLU(embed_size)
        self.norm2 = RMSNorm(embed_size)

    def forward(self, x, position_ids, mask=None):
        attn_out = self.attention(x, position_ids, mask)
        x = self.norm1(x + attn_out)
        ffn_out = self.ffn(x)
        return self.norm2(x + ffn_out)

# 最终 Transformer 结构

class Transformer(nn.Module):
    def __init__(self, embed_size, heads, num_layers, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.layers = nn.ModuleList([DecoderBlock(embed_size, heads) for _ in range(num_layers)])
        self.fc_out = nn.Linear(embed_size, vocab_size)

    def forward(self, x, position_ids=None, mask=None):
        x = self.embedding(x)

        # 生成 position_ids
        if position_ids is None:
            batch_size, seq_len = x.shape[:2]
            position_ids = torch.arange(seq_len, device=x.device).expand(batch_size, seq_len)

        for layer in self.layers:
            x = layer(x, position_ids, mask)

        return self.fc_out(x)
