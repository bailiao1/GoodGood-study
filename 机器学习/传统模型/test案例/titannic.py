import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"titanic\train.csv")
df2 = pd.read_csv(r"titanic\test.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())
df2['Age'] = df2['Age'].fillna(df2['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df2['Embarked'] = df2['Embarked'].fillna(df2['Embarked'].mode()[0])
df['FamilySize'] = df["SibSp"] + df["Parch"] + 1
df2['FamilySize'] = df2["SibSp"] + df2["Parch"] + 1


df.drop(columns=[ "Name", "Ticket", "Cabin"], inplace=True)       # 删除没必要的特征
df2.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)       # 删除没必要的特征

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})             # 性别转换为数值
df2["Sex"] = df2["Sex"].map({"male": 0, "female": 1})           # 性别转换为数值
df = pd.get_dummies(df, columns=["Embarked"])                   # 登岸口转为独热
df2 = pd.get_dummies(df2, columns=["Embarked"])                 # 登岸口转为独热

df[["Embarked_C", "Embarked_Q", "Embarked_S"]] = df[["Embarked_C", "Embarked_Q", "Embarked_S"]].astype(int)                # 编码转int
df2[["Embarked_C", "Embarked_Q", "Embarked_S"]] = df2[["Embarked_C", "Embarked_Q", "Embarked_S"]].astype(int)

x = df.drop(columns=["Survived"])                                                        
x2 = df2
y = df["Survived"]                                              # 将特征和标签拆分

X_train, X_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, random_state=100)                              # 分割数据集，测试集占比20%，保留随机种子

xgb_model = XGBClassifier(n_estimators=300, learning_rate=0.03, max_depth=10, random_state=42)                            # 调包定义xgboost模型
xgb_model.fit(X_train, y_train)

y_pred_xgb = xgb_model.predict(X_valid)
accuracy_xgb = accuracy_score(y_valid, y_pred_xgb)
print(f"XGBoost 准确率: {accuracy_xgb:.4f}")                                                                              # 还是很不错的哇，只是洗，补下数据，没做更进一步的交叉特征哇，增强什么，准确率有8成，数据优秀，架构nb


#---------------------------------------------------------------------------------------------------------------

# 整活小案例，近似逻辑回归，线性回归套壳
def zs(x):                                      # Z-score 归一化
  x = x.astype("f8")                            # 格式改一下，不然只能生成整数，小数会被截断
  n = x.shape[-1]
  for i in range(n):
    me = np.mean(x[:,i])
    st = np.std(x[:,i])
    if st == 0:
      x[:,i] = 0
    else:
      x[:,i] = (x[:,i] - me)/st
  return x
  
x = x.to_numpy()                               # panda表格转numpy矩阵
x2 = x2.to_numpy()
x = zs(x)                                      # 特征归一，缩小区间，否则模型学到的数值太大，下面的Sigmoid也拉不回来
x2 = zs(x2)

X_train, X_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, random_state=100)            # 拆分数据集

class xian():
    def __init__(self):
        self.coof_ = None
        self.intc_ = None
    def fit(self,x,y):
        x_b = np.c_[np.ones(len(x)), x]
        theta = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
        self.coof_ = theta[1:]
        self.intc_ = theta[0]

    def predict_proba(self, x):
        x_b = np.c_[np.ones(len(x)), x]
        z = x_b @ np.r_[self.intc_, self.coof_]
        return 1 / (1 + np.exp(-z))  # Sigmoid 激活

    def predict(self, x):
        return (self.predict_proba(x) >= 0.5).astype(int)


xi = xian()
xi.fit(X_train,y_train)                                          
print(xi.predict(X_valid[:100]))            # 输出当个乐子就行哈，能正常输出 1/0 就算赢 owo！
