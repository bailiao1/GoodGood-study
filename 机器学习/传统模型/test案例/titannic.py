import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"D:\dataji\titanic\train.csv")
df2 = pd.read_csv(r"D:\dataji\titanic\test.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())
df2['Age'] = df2['Age'].fillna(df2['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df2['Embarked'] = df2['Embarked'].fillna(df2['Embarked'].mode()[0])
df['FamilySize'] = df["SibSp"] + df["Parch"] + 1
df2['FamilySize'] = df2["SibSp"] + df2["Parch"] + 1


df.drop(columns=[ "Name", "Ticket", "Cabin"], inplace=True)       # 直接删除没必要的特征
df2.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)       # 直接删除没必要的特征

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})             # 性别转换为数值
df2["Sex"] = df2["Sex"].map({"male": 0, "female": 1})           # 性别转换为数值
df = pd.get_dummies(df, columns=["Embarked"])                   # 登岸口转为独热
df2 = pd.get_dummies(df2, columns=["Embarked"])                 # 登岸口转为独热

df[["Embarked_C", "Embarked_Q", "Embarked_S"]] = df[["Embarked_C", "Embarked_Q", "Embarked_S"]].astype(int)
df2[["Embarked_C", "Embarked_Q", "Embarked_S"]] = df2[["Embarked_C", "Embarked_Q", "Embarked_S"]].astype(int)


x = df.drop(columns=["Survived"])
x2 = df2
y = df["Survived"]

X_train, X_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, random_state=100)

xgb_model = XGBClassifier(n_estimators=300, learning_rate=0.03, max_depth=10, random_state=42)
xgb_model.fit(X_train, y_train)

y_pred_xgb = xgb_model.predict(X_valid)
accuracy_xgb = accuracy_score(y_valid, y_pred_xgb)
print(f"XGBoost 准确率: {accuracy_xgb:.4f}")
