import numpy as np

# 归一化（Normalization / Standardization）：
# - 目的不是让数值变小，而是为了让模型更容易学习：
# - 缩放特征值到统一范围（如 [0, 1] 或标准正态分布）
# - 加快收敛速度，提升训练稳定性，防止数值经过一系列乘法，输出把梯度炸飞 (如今更多问题还是数据特征不足，导致欠/过拟合，或者就是模型太复杂loss表面震荡，同样无法拟合...最缺的还是钱...算力，优良\原始数据)
# - 防止某些特征数值太大主导梯度，导致模型偏向
# - 保证每个特征在“同一量纲”下被公平看待，让模型关注的是"影响力"，不是"数值大小"


# Min-Max 归一化：将数据线性缩放到 [0,1] 或其他区间
# x' = (x - min(x)) / (max(x) - min(x))              # 可能会把某些特征变成0的哇,使用前先想想
x = np.random.randn(3,3)
def mm(x):
  n = x.shape[-1]
  for i in range(n):
    mi = np.min(x[:,i])
    ma = np.max(x[:,i])
    if mi == ma:
      x[:,i] = 0                                     # 如果不希望特征丢失，可以引入极小值来代替，或选择保留原值(但可能会影响数值分布，过大的值更会吸引模型的注意)
    else:
      x[:i] = (x[:i] - mi)/(ma - mi)
  return x


# Z-score 标准化（Standardization）：将数据转换为均值为 0，标准差为 1 的分布（也算一种“归一化”）
# x' = (x - 均值) / 标准差
def zs(x):
  n = x.shape[-1]
  for i in range(n):
    me = np.mean(x[:,i])
    st = np.std(x[:,i])
    if st == 0:
      x[:,i] = 0
    else:
      x[:,i] = (x[:,i] - me)/st
  return x



