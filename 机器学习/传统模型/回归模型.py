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


# LogisticRegression(max_iter=1000,solver="lbfgs")  # sklean写法： max_iter(最大迭代次数),solver="lbfgs"(最常用的优化方法)
# 逻辑回归是分类算法,适用于二分类问题(预测一件事成立的概率，大于50% 或 小于50% ，它是猫的概率有80% 不是的概率有 20%，所以推测出 1，是猫。0 则是其他动物)
# numpy手写实现：
class Logistic Regression():
    def __init__(self,lr=0.1,epochs=1000):                 # 输入学习率lr 以及 训练轮数
        self.lr = lr                                        
        self.epochs = epochs
        self.theta = None
        
    def sigmoid(self,x):                                   # sigmoid激活函数，将输出映射到[0,1]适用于二分类
        return 1 / (1 + np.exp(-x))                        # 1 / (1 + e^-x)

    def compute_loss(self,y,y_hat):                        # 计算交叉熵损失
        ep = 1e-15                                         # 设置个最小值，防止下面计算log时，出现0
        y_hat = np.clip(y_hat,ep ,1-ep)                                           # 限制数值大小
        return -np.mean(y * np.log(y_hat) + (1-y) * np.log(1 - y_hat))            

    def fit(self,x,y):
        m,n = x_b.shape[-2:]                               # 便利获取数据的样本数，特征数
        x_b = np.c_[np.ones((m,1)),x]                      # 添加偏置b
        self.theta = np.zeros(n)                           # 初始化w向量

        for epoch in range(epochs):                        # 设置训练循环，每轮预测一个值，进行一次梯度下降，不断向最优(极值点)靠近，步长由学习率控制，太大错过最优，太小走得太慢
            z = x @ theta                                  # 预测
            y_hat = self.sigmoid(z)                        

            gradient = x_b @ (y_hat - y) / m               # 计算梯度，loss的导数，找到前往极值点的方向
            self.theta -= self.lr * gradient               # 梯度下降 

            if epoch % 100 == 0:                           # 每100轮打印一次loss，方便监控
                loss = self.compute_loss(y,y_hat)
                print(f"Epoch: {epoch} , Loss: {loss:.4f}")

    def perdict(self,x):                                   # 训练完成后就可以预测了
        x_b = np.c_[]np.ones((x.shape[-2],1)),x]           # 同样给需要预测的样本添加偏置项
        out = self.sigmoid(x_b @ self.theta)               # 计算 xw+b
        return (out >= 0.5).astype('int')                  # 再将输出映射到[1,0]区间，转换成概率，概率大于等于0.5就输出1，否则为0
            

