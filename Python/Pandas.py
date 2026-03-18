import pandas as pd

# Series（一列）
s = pd.Series([10,20,30])
print(s)

#ＤataFrame（表格）
df = pd.DataFrame({
  "name": ["Bai","Hei"],
  "age": [25,30]
})

# 读取数据
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# 查看数据
df.head()      # 前5行
df.info()      # 数据结构
df.describe()  # 统计信息

# 选列/行
df["age"]         # 选一列
df["name","age"]  # 多列

df.iloc[0]     # 第一行（ 位置 0 ）
df.loc[0]      # 按索引（ index标签为 0 ）

# 条件筛选
df[df["age"] >25]

# 新增列
df["age_plus_1"] = df["age"] + 1

# 删除
df.drop("age", axis=1)   # 行为 axis=0

# 处理缺失值
df.dropna()              # 删除空值 
df.fillna(0)             # 填充

# 分组
df = pd.DataFrame({
    '产品': ['A', 'B', 'A', 'B', 'A', 'B'],
    '销售额': [100, 200, 150, 250, 120, 180],
    '地区': ['北', '北', '南', '南', '东', '东']
})

# 1. 按产品分组，计算每种产品的总销售额
df.groupby('产品')['销售额'].sum()

# 2. 按产品和地区分组，计算平均销售额
df.groupby(['产品', '地区'])['销售额'].mean()

# 3. 使用 agg 同时计算总和与计数
df.groupby('产品')['销售额'].agg(['sum', 'count'])


# 时间数据
df = pd.DataFrame({"date": ["2025-01-01","2025-02-01"]})
df["date"] = pd.to_datetime(df["date"])

# 提取时间信息（用.dt访问时间属性）
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.weekday

# 时间筛选
df[df["date"] > "2025-01-15"]
df[df["data"] >= "2025-01-01" & (df["date"] <= "2024-01-31")]

# 设置时间索引
df = df.set_index("date")
# - 之后可以使用
df.loc["2025-01-01":"2025-01-31"]    # 检索 2025-1-1 到 2025-1-31 的信息

# 时间重采样（日D，月M，年Y，小时H）
df.resample("M").sum()     # 按月
df.resample("D").mean()    # 按日

# 时间偏移(加减时间)
df["date"] + pd.Timedelta(days=1)
df["date"] - pd.Timedelta(hours=2)

# 时间差计算
df["diff"] = df["date"].diff()                  # df.diff(periods=1, axis=0) 计算元素与同一轴上 前一个元素 的差值
df["gap"] = df["date"] - df["date"].shift(1)    # df.shift(periods=1,axis=0) 将数据沿指定轴平移指定步数

