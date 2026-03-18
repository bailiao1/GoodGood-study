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
df[df[]]
