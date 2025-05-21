import random

# 基础随机数
print(random.random())        # 0 <= x < 1
print(random.uniform(1, 10))  # 浮点数
print(random.randint(1, 10))  # 整数，包括10
print(random.randrange(1, 10, 2))  # 奇数

# 序列相关
lst = [1, 2, 3, 4, 5]
print(random.choice(lst))
print(random.choices(lst, k=3))       # 有放回
print(random.sample(lst, k=3))        # 无放回
random.shuffle(lst)
print(lst)

# 分布相关
print(random.gauss(0, 1))  # 均值为0，标准差为1

# 控制随机性
random.seed(42)
print(random.randint(1, 100))
