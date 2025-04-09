import torch

def apply_rotary_pos_emb(x, position_ids, theta=10000.0):
    """
    RoPE 旋转位置编码
    x: 输入 Tensor (batch, seq_len, dim)
    position_ids: 位置索引 (batch, seq_len)
    theta: 角频率
    """
    batch_size, seq_len, dim = x.shape
    assert dim % 2 == 0, "Embedding维度必须是偶数"

    half_dim = dim // 2        # 一半维度进行旋转
    index = torch.arange(half_dim, dtype=torch.float32, device=x.device)

    # 计算 theta^(-2i/dim)
    theta = theta ** (-2 * index / half_dim)

    # 计算旋转角度 θ_p
    position = position_ids.unsqueeze(-1).float()     # (batch, seq_len, 1)
    theta_p = position * theta                        # (batch, seq_len, half_dim)

    # 计算 cos(θ_p) 和 sin(θ_p)
    cos_theta = torch.cos(theta_p)
    sin_theta = torch.sin(theta_p)

    # 取输入的前半部分和后半部分
    x1, x2 = x[..., :half_dim], x[..., half_dim:]

    # 旋转计算
    x_rotated = torch.cat([x1 * cos_theta - x2 * sin_theta,
                           x1 * sin_theta + x2 * cos_theta], dim=-1)

    return x_rotated
