import numpy as np


# model = LinearRegression()                                  # 线性回归
# 手写版线性回归
# import numpy as np
#
# class LinearRegressionScratch:                            # 定义类
#     def __init__(self):                                   # init初始化类
#         self.coef_ = None                                 # 设self.coef(系数)
#         self.intercept_ = None                            # 设self.intercept_(截距)
#
#     def fit(self, X, y):                                          # 定义方法(传入训练数据,结果)
#         X_b = np.c_[np.ones((X.shape[0], 1)), X]                  # 增加偏置项
#         theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)   # 正规方程求解
#         self.intercept_ = theta[0]                                # 偏置项
#         self.coef_ = theta[1:]                                    # 真正的模型参数
#
#     def predict(self, X):                                         # 定义方法(传入数据，预测结果)
#         X_b = np.c_[np.ones((X.shape[0], 1)), X]                  # 也要增加偏置项
#         return X_b @ np.r_[self.intercept_, self.coef_]           # 组合参数(theta)
#
# # 测试
# X = np.array([[1], [2], [3], [4]])
# y = np.array([2, 3, 4, 5 ])
#
# model = LinearRegressionScratch()
# model.fit(X, y)
# print(model.predict(np.array([[5]])))  # 预测 5 的值        # [6.]

# 岭回归   Ridge(alpha=1.0)  # λ = 1.0(alpha控制L2正则强度,使一些特征权重缩小，限制模型的复杂度)
#         theta = np.linalg.inv(X_b.T.dot(X_b)+λ*I).dot(X_b.T).dot(y)    (L2正则公式,I=单位矩阵）
# Lasso   Lasso(alpha=0.1)  # λ = 0.1(alpha控制L1正则强度,使一些特征权重化0,达到特征选择的效果)
#         数学公式中对权重使用绝对值,而L2使用平方.因此L2只会缩小权重，而L1可以直接让一些特征权重化0
# 但L1正则化因为包含|theta|(绝对值),不能直接用矩阵求逆，所以需要用优化算法（梯度下降、坐标下降等）来求解
# 手写 Lasso 梯度下降
# class LassoRegression:                                        # 定义类
#     def __init__(self, alpha=0.1, lr=0.01, max_iter=1000):    # 初始化实例对象
#         self.alpha = alpha                                    # 正则化系数 λ
#         self.lr = lr                                        # 学习率
#         self.max_iter = max_iter                            # 最大迭代
#         self.theta = None                                   # 定义参数(theta)
#
#     def soft_thresholding(self, value, alpha):
#         """ L1 正则化的软阈值函数 """
#         if value > alpha:
#             return value - alpha
#         elif value < -alpha:
#             return value + alpha
#         else:
#             return 0
#
#     def fit(self, X, y):                                    # 定义训练方法
#         X_b = np.c_[np.ones((X.shape[0], 1)), X]            # 增加偏置项
#         m, n = X_b.shape                                    # m代表样本数(行）,n代表特征数(列)
#         self.theta = np.zeros(n)                            # 全零矩阵,初始化参数格式,用于后续计算
#                                                              # theta的格式永远和特征数n挂钩，否则无法进行计算
#         for _ in range(self.max_iter):
#             y_pred = X_b @ self.theta
#             gradient = (2 / m) * X_b.T @ (y - y_pred)
#
#             # L1 正则化
#             for j in range(n):
#                 gradient[j] = self.soft_thresholding(gradient[j], self.alpha)

# 向量化版本L1正则，无需定义soft方法，无需使用for循环
#             gradient = np.sign(gradient) * np.maximum(np.abs(gradient) - self.alpha, 0)
#
#             self.theta -= self.lr * gradient
#
#     def predict(self, X):
#         X_b = np.c_[np.ones((X.shape[0], 1)), X]              # 增加偏置项
#         return X_b @ self.theta                               # 计算预测值
#
# # # 测试数据
# X = np.array([[1], [2], [3], [4]])
# y = np.array([2, 2.8, 4, 4.8])
#
# # 训练 Lasso 回归
# lasso = LassoRegression(alpha=0.1, lr=0.05, max_iter=1000)
# lasso.fit(X, y)
# print(lasso.predict(np.array([[5]])))
# print("Lasso 计算的 theta:", lasso.theta)      # Lasso 计算的 theta: [0. 0.]

# 逻辑回归 LogisticRegression(max_iter=1000,solver="lbfgs")  # max_iter(最大迭代次数),solver="lbfgs"(最常用的优化方法)
# 逻辑回归是分类算法,适用于二分类问题

# model = SVC(kernel="linear")   # 线性核                   # SVC(支持向量机)
# SVM（支持向量机）用于分类，它寻找最佳超平面来分隔数据。

#         KMeans(n_clusters=3, random_state=42)            # K-Means 聚类, n_clusters=3(分成三类)
# 无监督学习,自动把数据分成K组,找到每组的中心点(聚类中心),计算数据点到中心点的距离,重新分配分类。
# model.fit(目标特征)
# print("样本的聚类类别:", kmeans.labels_)                   # 输出每个样本的分类

#         PCA(n_components=2)  # 降维到 2 维
# X_pca = model.fit_transform(目标特征)
# PCA是降维方法,可以去掉冗余信息(降低特征维度),提取最有用的特征。


# model.fit(特征集,结果集)                            # 模型训练
# 预测集 = model.predict(特征集)                      # 模型使用




