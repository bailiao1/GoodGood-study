import numpy as np

# 定义感知机
class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.randn(input_size)  # 随机初始化权重
        self.bias = np.random.randn()  # 随机初始化偏置

    def forward(self, x):
        output = np.dot(self.weights, x) + self.bias  # 计算WX + b
        return 1 if output >= 0 else 0  # 阈值激活函数（简单的二分类）

# 创建感知机（假设输入有3个特征）
perceptron = Perceptron(3)

# 测试一个输入样本
sample = np.array([0.5, -0.2, 0.8])
result = perceptron.forward(sample)
print("感知机输出:", result)


# 单层神经元
def relu(x):                                                # 激活函数：ReLU 太 tm 重要啦
    return np.maximum(0, x)                                 # 什么？你的趋势应该是继续上升？不行，你必须是0（去死~）

class Neuron:                                               # 定义一个简单的神经元
    def __init__(self, input_size):
        self.weights = np.random.randn(input_size)          # 随机初始化权重
        self.bias = np.random.randn()                       # 随机初始化偏置

    def forward(self, x):
        output = np.dot(self.weights, x) + self.bias        # 计算 WX + b
        return relu(output)                                 # 使用 ReLU 激活函数

neuron = Neuron(3)                                          # 创建神经元（输入有 3 个特征）
sample_input = np.array([0.5, -0.2, 0.8])                   # 传入一个样本数据
output = neuron.forward(sample_input)
print("神经元输出:", output)


# 多层感知器
def relu(x):                                                # 激活函数（ReLU 和 Sigmoid）
    return np.maximum(0, x)

def sigmoid(x):                                             # Sigmoid能将输入映射到 (0,1) 之间，使输出转换为概率，适应于二分类任务的输出层
    return 1 / (1 + np.exp(-x))

class MLP_XOR:                                              # 定义 MLP 网络（1 隐藏层）
    def __init__(self):                                     # 初始化权重和偏置
        self.W1 = np.random.randn(2, 2)                     # 随机W1,两个特征
        self.b1 = np.random.randn(2)                        # 随机偏置
        self.W2 = np.random.randn(2, 1)                     # 随机W2,一个特征
        self.b2 = np.random.randn(1)                        # 随机偏置,数量与权重对应

    def forward(self, x):
        # 隐藏层计算
        hidden = relu(np.dot(x, self.W1) + self.b1)
        # 输出层计算
        output = sigmoid(np.dot(hidden, self.W2) + self.b2)
        return output

# 创建 MLP 模型
mlp = MLP_XOR()

# 训练数据（XOR 输入）
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# 计算 MLP 预测结果
predictions = mlp.forward(X)
print("MLP 预测输出:", predictions)



# 感知器示例二
def relu(x):                                                # 激活函数
    return np.maximum(0, x)
def softmax(x):                                             # softmax也是将输入转换为概率分布，但是是所有类别的概率总和为 1，也就是归一化，适用于多分类任务
    exp_x = np.exp(x - np.max(x))                           # 防止指数溢出
    return exp_x / exp_x.sum(axis=0, keepdims=True)

# 定义 MLP
class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(hidden_size, input_size)
        print(self.W1.shape)
        self.b1 = np.random.randn(hidden_size)
        self.W2 = np.random.randn(output_size, hidden_size)
        print(self.W2.shape)
        self.b2 = np.random.randn(output_size)

    def forward(self, x):                                  
        x = x.reshape(1, -1)
        # 隐藏层计算
        print(x.shape)
        self.hidden = relu(np.dot(x,self.W1.T) + self.b1)
        # 输出层计算
        output = softmax(np.dot(self.hidden,self.W2.T) + self.b2)
        return output

# 创建一个 MLP（输入 3 维，隐藏层 5 维，输出 2 维）
mlp = MLP(3, 5, 2)
# 传入一个样本数据
sample_input = np.array([0.5, -0.2, 0.8])
output = mlp.forward(sample_input)
print("MLP 输出:", output)




# 反向传播（模型的权重校准，梯度下降啊等等。。。）
def relu(x):                            # 激活函数
    return np.maximum(0, x)
def relu_derivative(x):
    return (x > 0).astype(float)       # ReLU 的导数：大于 0 时为 1，小于等于 0 时为 0
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # 防止指数溢出
    return exp_x / exp_x.sum(axis=0, keepdims=True)
# MLP 反向传播
class MLP:
    def __init__(self, input_size, hidden_size, output_size, lr=0.01):
        self.W1 = np.random.randn(hidden_size, input_size)
        self.b1 = np.random.randn(hidden_size)
        self.W2 = np.random.randn(output_size, hidden_size)
        self.b2 = np.random.randn(output_size)
        self.lr = lr                                                             # 学习率

    def forward(self, x):
        self.x = x                                                               # 记录输入
        self.hidden = relu(np.dot(self.W1, x) + self.b1)                         # 隐藏层
        self.output = softmax(np.dot(self.W2, self.hidden) + self.b2)            # 输出层（也就是最后的总结层）
        return self.output

    def backward(self, y_true):                             # 计算损失的梯度（Softmax 交叉熵的导数）梯度就是loss的导数啦，指引正确的方向。但小心步子（学习率）太大，一山更有一山高（局部最优）
        loss_grad = self.output - y_true                    

        # 计算 W2 和 b2 的梯度
        dW2 = np.outer(loss_grad, self.hidden)              # np.outer计算两个向量的外积
        db2 = loss_grad

        # 计算隐藏层的梯度
        hidden_grad = np.dot(self.W2.T, loss_grad) * relu_derivative(self.hidden)

        # 计算 W1 和 b1 的梯度
        dW1 = np.outer(hidden_grad, self.x)
        db1 = hidden_grad

        # 更新参数
        self.W2 -= self.lr * dW2                            # 梯度下降（w = w-rt）权重 = 权重 - 学习率*梯度
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

# 创建 MLP（输入 3 维，隐藏层 5 维，输出 2 维）
mlp = MLP(3, 5, 2, lr=0.01)
# 训练数据（输入 & 真实标签）
sample_input = np.array([0.5, -0.2, 0.8])
true_label = np.array([1, 0])  # 假设正确类别是第一个类
# 前向传播
output = mlp.forward(sample_input)
# 反向传播（更新 W 和 b）
mlp.backward(true_label)
print("MLP 预测输出:", output)


# 完整感知器
def relu(x):                                        # 激活函数
    return np.maximum(0, x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# 计算损失（交叉熵）
def binary_cross_entropy(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred + 1e-8) + (1 - y_true) * np.log(1 - y_pred + 1e-8))
# 计算激活函数的导数
def relu_derivative(x):
    return np.where(x > 0, 1, 0)
def sigmoid_derivative(x):
    return x * (1 - x)
# MLP 模型
class MLP_XOR:
    def __init__(self, learning_rate=0.1):
        np.random.seed(42)                                  # 设定随机种子，确保可复现
        self.W1 = np.random.randn(2, 2)                     # 输入 -> 隐藏层权重
        self.b1 = np.random.randn(2)                        # 隐藏层偏置
        self.W2 = np.random.randn(2, 1)                     # 隐藏层 -> 输出层权重
        self.b2 = np.random.randn(1)                        # 输出层偏置
        self.learning_rate = learning_rate

    def forward(self, x):
        self.hidden_input = np.dot(x, self.W1) + self.b1
        self.hidden_output = relu(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.W2) + self.b2
        self.final_output = sigmoid(self.final_input)
        return self.final_output

    def backward(self, x, y_true):
        m = x.shape[0]  # 样本数量
        y_pred = self.final_output

        # 计算梯度（误差的反向传播）
        dL_dy = (y_pred - y_true) / m     # 交叉熵损失对 y_pred 的导数

        # 计算输出层梯度
        dL_dW2 = np.dot(self.hidden_output.T, dL_dy * sigmoid_derivative(y_pred))
        dL_db2 = np.sum(dL_dy * sigmoid_derivative(y_pred), axis=0)

        # 计算隐藏层梯度
        d_hidden = np.dot(dL_dy * sigmoid_derivative(y_pred), self.W2.T) * relu_derivative(self.hidden_input)
        dL_dW1 = np.dot(x.T, d_hidden)
        dL_db1 = np.sum(d_hidden, axis=0)

        # 更新参数（梯度下降）
        self.W1 -= self.learning_rate * dL_dW1
        self.b1 -= self.learning_rate * dL_db1
        self.W2 -= self.learning_rate * dL_dW2
        self.b2 -= self.learning_rate * dL_db2

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            self.forward(X)  # 前向传播
            self.backward(X, y)  # 反向传播

            # 每 1000 轮打印一次损失
            if epoch % 1000 == 0:
                loss = binary_cross_entropy(y, self.final_output)
                print(f"Epoch {epoch}, Loss: {loss:.5f}")

# 训练数据（XOR 输入）
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])  # XOR 输出
# 训练 MLP
mlp = MLP_XOR(learning_rate=0.1)
mlp.train(X, y, epochs=10000)
# 测试模型
print("训练完成！测试 XOR 结果：")
for i in range(len(X)):
    pred = mlp.forward(X[i].reshape(1, -1))
    print(f"输入: {X[i]}, 预测输出: {pred[0][0]:.5f}")
