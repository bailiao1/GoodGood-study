import numpy as np

# Min-Max 归一化：将数据线性缩放到 [0,1] 或其他区间
# x' = (x - min(x)) / (max(x) - min(x))              # 会把某些特征变成0的哇,使用前先想想
x = np.random.randn(3,3)
def mm(x):
  m = x.shape[-1]
  for i in range(m):
    mi = np.min(x[:,i])
    ma = np.max(x[:,i])
    if mi == ma:
      x[:,i] = 0
    else:
      x[:i] = (x[:i] - mi)/(ma - mi)
  return x


# Z-score 标准化（Standardization）：将数据转换为均值为 0，标准差为 1 的分布（也算一种“归一化”）
# x' = (x - 均值) / 标准差
def zs(x):
  n,m = x.shape[-2:]
  for i in range(m):
    me = np.mean(x[:,i])
    st = np.std(x[:,i])
    if st == 0;
      x[:,i] = 0
    else:
      x[:,i] = (x[:,i] - me)/st
  return x
