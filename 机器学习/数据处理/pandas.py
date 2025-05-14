import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],                       #          Name  Age         City
    "Age": [25, 30, 35],                                       #    0    Alice   25     New York
    "City": ["New York", "Los Angeles", "Chicago"]             #    1      Bob   30  Los Angeles
}                                                              #    2  Charlie   35      Chicago
df = pd.DataFrame(data)             # 创建 DataFrame
print(df)
df = pd.read_csv("data.csv")        # 读取 CSV 文件，返回 DataFrame（表格）
print(df.head())                    # 显示前5行

print(df.info())                    # 查看数据类型,缺失值
print(df.describe())                # 查看数据的基本统计信息（均值,方差,最大值,最小值）

print(df["Age"].mean())             # 计算 "Age" 列的平均值
print(df.shape)                     # 输出 (行数, 列数)
print(df.columns)                   # 查看所有列名

print(df["Name"])                   # 选取某一列
print(df.iloc[0])                   # 选取第一行
print(df.loc[df["Age"] > 30])       # 选取 Age 大于 30 的行
  
df.dropna()                         # 删除缺失值
df.fillna("Unknown")                # 填充缺失值
df.fillna(df.mean(), inplace=True)  # 用均值填充缺失值
df.drop_duplicates()                # 删除重复值

print(df["销售额"].mean())           # 计算均值
print(df["销售额"].median())         # 计算中位数
print(df["销售额"].var())            # 计算方差
print(df["销售额"].std())            # 计算标准差
print(df.corr())                    # 计算所有列之间的相关性

# 可视化数据
# import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
import seaborn as sns
# 绘制分布
df = pd.read_csv("D:\dataset\California Wildfire Damage.csv")
df.fillna("Unknown")
plt.figure(figsize=(8,5))         # histplot() 绘制直方图,bins=30 表示分成 30 组,kde=True 加上密度曲线
sns.histplot(df["Estimated_Financial_Loss (Million $)"],bins=100,kde=True)      # 适合表示同位损失的次数
plt.show()



# 读取数据
df = pd.read_csv(r"D:\dataset\California Wildfire Damage.csv")

# 预处理：去掉列名前后空格，避免拼写错误
df.columns = df.columns.str.strip()

# 转换 "Estimated_Financial_Loss (Million $)" 为数值（防止数据类型错误）
df["Estimated_Financial_Loss (Million $)"] = pd.to_numeric(df["Estimated_Financial_Loss (Million $)"], errors="coerce")

# 处理缺失值（如果有 NaN，填充 0）
df["Estimated_Financial_Loss (Million $)"].fillna(0, inplace=True)

# 选择前 20 个数据（防止 X 轴过长）
df_sample = df.head(20)

# 绘制柱状图
plt.figure(figsize=(12, 6))
sns.barplot(x="Incident_ID", y="Estimated_Financial_Loss (Million $)", data=df_sample)

# 旋转 X 轴标签，防止重叠
plt.xticks(rotation=45)

# 添加轴标签和标题
plt.xlabel("事件编号 (Incident ID)")
plt.ylabel("经济损失（百万美元）")
plt.title("不同事件的经济损失")

# 显示图表
plt.show()



# 泰坦尼克号数据集处理
# 1.查看数据集
df = pd.read_csv(r'D:\dataset\Titanic\train.csv')
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.width', 1000)  # 设置最大宽度，防止自动换行
print(df.head())
print(f"数据集大小:{df.shape}")                  # 数据集大小:(891, 12)   # 891行,12列(891条数据,12个特征值)
print(f"列名:{df.columns.tolist()}")            # 列名:['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                                                     'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
print(df.info())
print(df.describe())
print(f"缺少{df.isnull().sum()}")               # 缺少177个Age,687个Cabin,2个Embarked

# 2.处理数据集
df = pd.read_csv(r'D:\dataset\Titanic\train.csv')
df["Age"] = df["Age"].fillna(df['Age'].median())                  # 年龄具有连续性,用中位数填充
df["Cabin"] = df["Cabin"].fillna("Unknown")                       # 舱位缺少太多,但考虑可能影响生存率,保留,但填补上未知
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # 只缺少两个Embarked,直接用众数填充
# print(f"缺少{df.isnull().sum()}")                               # 再次检查值是否缺少

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})              # 数据填充完,转换字符类型,字符串类型需要转换成数值格式
df = pd.get_dummies(df, columns=["Embarked"])                    # 使用独热编码转换Embarked(登船口岸)的数值
print(df.info())                                                 # 再次查看类型

df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)         # 删除对结果预测无用的特征,如票号,姓名
df[["Embarked_C", "Embarked_Q", "Embarked_S"]] = df[["Embarked_C", "Embarked_Q", "Embarked_S"]].astype(int)   # 转int
X = df.drop(columns=["Survived"])  # 训练特征
y = df["Survived"]  # 预测目标
