import numpy as np

# 恭迎回归老祖！！！

class LinearRegressionScratch:                            # 定义类
    def __init__(self):                                   # init初始化类
        self.coef_ = None                                 # 设self.coef(系数)
        self.intercept_ = None                            # 设self.intercept_(截距)

    def fit(self, X, y):                                          # 定义方法(传入训练数据,结果)
        X_b = np.c_[np.ones((X.shape[0], 1)), X]                  # 增加偏置项(生成一列1，用np.c_粘到x上去)
        theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)   # 正规方程求解(最小二乘法): A.T(AA.T)^-1 y
        self.intercept_ = theta[0]                                # 重新剥离出偏置项(之前生成的那一列1)
        self.coef_ = theta[1:]                                    # 真正的模型权重参数

    def predict(self, X):                                         # 定义方法(传入数据，预测结果)
        X_b = np.c_[np.ones((X.shape[0], 1)), X]                  # 也要增加偏置项
        return X_b @ np.r_[self.intercept_, self.coef_]           # 组合参数(theta),np.r_行连接      # y = wx + b = theta[0]*1 + theta[1:]*x = [1,x] @ [[b],[w]] 

# 测试
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 3, 4, 5 ])                                       # y = x+1

model = LinearRegressionScratch()
model.fit(X, y)
print(model.predict(np.array([[5]])))  # 预测 5 的值        # [6.]




