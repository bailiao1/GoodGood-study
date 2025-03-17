import numpy as np

# 岭回归   Ridge(alpha=1.0)  # λ = 1.0(alpha控制L2正则强度,使一些特征权重缩小，限制模型的复杂度)
#         theta = np.linalg.inv(X_b.T.dot(X_b)+λ*I).dot(X_b.T).dot(y)    (L2正则公式,I=单位矩阵）

# Lasso   Lasso(alpha=0.1)  # λ = 0.1(alpha控制L1正则强度,使一些特征权重化0,达到特征选择的效果)
#         数学公式中对权重使用绝对值,而L2使用平方.因此L2只会缩小权重，而L1可以直接让一些特征权重化0
# 但L1正则化因为包含|theta|(绝对值),不能直接用矩阵求逆，所以需要用优化算法（梯度下降、坐标下降等）来求

# 手写 Lasso 梯度下降
class LassoRegression:                                        # 定义类
    def __init__(self, alpha=0.1, lr=0.01, max_iter=1000):    # 初始化实例对象
        self.alpha = alpha                                    # 正则化系数 λ
        self.lr = lr                                        # 学习率
        self.max_iter = max_iter                            # 最大迭代
        self.theta = None                                   # 定义参数(theta)

    def soft_thresholding(self, value, alpha):
        """ L1 正则化的软阈值函数 """
        if value > alpha:
            return value - alpha
        elif value < -alpha:
            return value + alpha
        else:
            return 0

    def fit(self, X, y):                                    # 定义训练方法
        X_b = np.c_[np.ones((X.shape[0], 1)), X]            # 增加偏置项
        m, n = X_b.shape                                    # m代表样本数(行）,n代表特征数(列)
        self.theta = np.zeros(n)                            # 全零矩阵,初始化参数格式,用于后续计算
                                                             # theta的格式永远和特征数n挂钩，否则无法进行计算
        for _ in range(self.max_iter):
            y_pred = X_b @ self.theta
            gradient = (2 / m) * X_b.T @ (y - y_pred)

            # L1 正则化
            for j in range(n):
                gradient[j] = self.soft_thresholding(gradient[j], self.alpha)

# 向量化版本L1正则，无需定义soft方法，无需使用for循环
            gradient = np.sign(gradient) * np.maximum(np.abs(gradient) - self.alpha, 0)

            self.theta -= self.lr * gradient

    def predict(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]              # 增加偏置项
        return X_b @ self.theta                               # 计算预测值

# 测试数据
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 2.8, 4, 4.8])

# 训练 Lasso 回归
lasso = LassoRegression(alpha=0.1, lr=0.05, max_iter=1000)
lasso.fit(X, y)
print(lasso.predict(np.array([[5]])))
print("Lasso 计算的 theta:", lasso.theta)      


# 逻辑回归 LogisticRegression(max_iter=1000,solver="lbfgs")  # max_iter(最大迭代次数),solver="lbfgs"(最常用的优化方法)
# 逻辑回归是分类算法,适用于二分类问题
