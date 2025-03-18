import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题
import numpy as np
import torch                                                # PyTorch 导入
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.optim.lr_scheduler import StepLR




# 查看状态
# print("PyTorch 版本:", torch.__version__)
# print("CUDA 是否可用:", torch.cuda.is_available())
# if torch.cuda.is_available():
#     print("CUDA 版本:", torch.version.cuda)
#     print("GPU 数量:", torch.cuda.device_count())
#     print("当前 GPU:", torch.cuda.get_device_name(0))


# 创建张量
# a = torch.tensor([1.0, 2.0, 3.0])
# print("张量 a:", a)
#
# 创建随机张量
# b = torch.rand(2, 3)  # 2行3列
# print("随机张量 b:\n", b)
#
# 创建全 0 或全 1 张量
# c = torch.zeros(3, 3)
# d = torch.ones(2, 2)
# print("全 0 张量 c:\n", c)
# print("全 1 张量 d:\n", d)
#
# 创建单位矩阵
# e = torch.eye(3)  # 3x3 单位矩阵
# print("单位矩阵 e:\n", e)
#
# 生成 GPU 张量
# gpu_tensor = torch.tensor([1, 2, 3], device="cuda")  # 直接在 GPU 上创建
# print("GPU 张量:", gpu_tensor)


# 基本数学运算
# a = torch.tensor([1, 2, 3])
# b = torch.tensor([4, 5, 6])
#
# # 加法
# print("加法:", a + b)
#
# # 减法
# print("减法:", a - b)
#
# # 乘法（逐元素相乘）
# print("乘法:", a * b)
#
# # 除法
# print("除法:", a / b)
#
# # 幂运算
# print("平方:", a ** 2)

# 矩阵运算
# A = torch.tensor([[1, 2], [3, 4]])
# B = torch.tensor([[5, 6], [7, 8]])
#
# # 矩阵加法
# print("矩阵加法:\n", A + B)
# # 矩阵乘法（逐元素）
# print("逐元素乘法:\n", A * B)
# # 矩阵点积（矩阵乘法）
# print("矩阵点积:\n", torch.matmul(A, B))  # 或者 A @ B
# # 计算矩阵转置
# print("矩阵转置:\n", A.T)

# torch.transpose(A,dim0,dim1)  # 更高级的转置，对shape进行操作，交换dim0 和 dim1 的位置,适用于高维度


# 使用GPU加速运算
# if torch.cuda.is_available():      # 确保 CUDA 可用
#     device = torch.device("cuda")  # 选择 GPU
# else:
#     device = torch.device("cpu")   # 选择 CPU
# # 在 GPU 上创建张量
# A = torch.rand(1000, 1000, device=device)
# B = torch.rand(1000, 1000, device=device)
# # GPU 加速矩阵乘法
# C = torch.matmul(A, B)
# print("计算完成，张量在设备:", C.device)


# 自动求导（Autograd）
# x = torch.tensor(2.0, requires_grad=True)       # 创建一个可计算梯度的张量
# # 计算 y = x^2
# y = x ** 2
# # 反向传播（计算 dy/dx）
# y.backward()
# # 输出梯度(导数)
# print("x 的梯度:", x.grad)  # x 的梯度: tensor(4.)     # 2*x = 4


# 计算多变量梯度
# x = torch.tensor(3.0, requires_grad=True)
# # 计算 z = x^2 + 3x + 5
# z = x**2 + 3*x + 5
# # 反向传播
# z.backward()
# # 输出梯度
# print("x 的梯度:", x.grad)  # x 的梯度: tensor(9.)     # 2*x + 3 = 2*3 + 3 = 9


# 计算多个输出对多个输入的梯度
# x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
# # 计算 y = x^2
# y = x ** 2
# # 反向传播（对 y 的所有元素求梯度）
# y.backward(gradient=torch.ones_like(y))
# print("x 的梯度:", x.grad)  # x 的梯度: tensor([2., 4., 6.])      # 2*x


# 关闭梯度计算（加速推理）
# x = torch.tensor(5.0, requires_grad=True)
# with torch.no_grad():
#     y = x ** 2
#     print(y)  # 25.0，但不会计算梯度


# 训练线性回归模型
# x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])  # 输入 x
# y_train = torch.tensor([[5.0], [7.0], [9.0], [11.0]]) # 目标 y = 2x + 3
#
# # 定义模型（线性回归 y = Wx + b）
# W = torch.randn(1, requires_grad=True)  # 初始化权重
# b = torch.randn(1, requires_grad=True)  # 初始化偏置
#
# # 训练循环
# learning_rate = 0.01
# epochs = 100  # 训练 100 轮
#
# for epoch in range(epochs):
#     # 计算预测值
#     y_pred = W * x_train + b
#
#     # 计算损失（均方误差 MSE）
#     loss = ((y_pred - y_train) ** 2).mean()
#
#     # 反向传播计算梯度
#     loss.backward()
#
#     # 更新参数（手动梯度下降）
#     with torch.no_grad():
#         W -= learning_rate * W.grad
#         b -= learning_rate * b.grad
#
#     # 清空梯度（避免累积）
#     W.grad.zero_()
#     b.grad.zero_()
#
#     # 每 10 轮打印一次损失
#     if (epoch + 1) % 10 == 0:
#         print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}, W: {W.item():.4f}, b: {b.item():.4f}")
#
# # 训练完成后，看看最终的 W 和 b
# print("\n训练完成！")
# print(f"最终 W: {W.item():.4f}, b: {b.item():.4f}")


# nn.Module

# 准备数据
# x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
# y_train = torch.tensor([[5.0], [7.0], [9.0], [11.0]])  # y = 2x + 3

# 定义神经网络（继承 nn.Module）
# class LinearRegressionModel(nn.Module):
#     def __init__(self):
#         super(LinearRegressionModel, self).__init__()
#         self.linear = nn.Linear(1, 1)  # 线性层：输入 1 维，输出 1 维
#
#     def forward(self, x):
#         return self.linear(x)
# 创建模型
# model = LinearRegressionModel()
#
# # 定义损失函数和优化器
# criterion = nn.MSELoss()  # 均方误差损失
# optimizer = optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降（SGD）
#
# # 训练模型
# epochs = 100
# for epoch in range(epochs):
#     # 前向传播
#     y_pred = model(x_train)
#     loss = criterion(y_pred, y_train)
#
#     # 反向传播 & 更新参数
#     optimizer.zero_grad()  # 清空梯度
#     loss.backward()  # 计算梯度
#     optimizer.step()  # 更新参数
#
#     # 每 10 轮打印一次损失
#     if (epoch + 1) % 10 == 0:
#         print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
#
# # 训练完成
# print("\n训练完成！模型参数:")
# for name, param in model.named_parameters():
#     print(f"{name}: {param.item():.4f}")


# 感知器模型
# x_train = torch.linspace(-1, 1, 100).reshape(-1, 1)  # 100 个点，形状 (100, 1)   # 生成数据（模拟非线性关系）
# y_train = x_train**3 + 0.3 * torch.randn(x_train.size())  # 目标 y = x^3 + 噪声
#
# # 定义 MLP 神经网络（多层感知机）
# class MLP(nn.Module):
#     def __init__(self):
#         super(MLP, self).__init__()
#         self.hidden = nn.Linear(1, 10)  # 隐藏层：1 输入 -> 10 神经元
#         self.output = nn.Linear(10, 1)  # 输出层：10 -> 1
#
#     def forward(self, x):
#         x = torch.relu(self.hidden(x))  # ReLU 激活
#         x = self.output(x)  # 输出层（回归任务，不用 Softmax）
#         return x
#
# # 创建 MLP 模型
# model = MLP()
#
# # 定义损失函数 & 优化器
# criterion = nn.MSELoss()  # 均方误差（MSE）
# optimizer = optim.Adam(model.parameters(), lr=0.01)  # Adam 优化器
#
# # 训练模型
# epochs = 1000  # 训练 1000 轮
# for epoch in range(epochs):
#     y_pred = model(x_train)  # 前向传播
#     loss = criterion(y_pred, y_train)  # 计算损失
#
#     optimizer.zero_grad()  # 清空梯度
#     loss.backward()  # 计算梯度
#     optimizer.step()  # 更新参数
#
#     if (epoch + 1) % 100 == 0:
#         print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
#
# # 训练完成
# print("\n训练完成！")
# for name, param in model.named_parameters():
#     print(f"{name} 平均值: {param.mean().item():.4f}")


# CNN
#
# 数据加载（MNIST）
transform = transforms.Compose([
    transforms.ToTensor(),                                # 转换为 PyTorch Tensor
    transforms.Normalize((0.5,), (0.5,))        # 归一化
])

train_dataset = torchvision.datasets.MNIST(root="./data", train=True, transform=transform, download=True)
test_dataset = torchvision.datasets.MNIST(root="./data", train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)
#
# # 定义 CNN 网络
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)  # 卷积层1（输入通道=1，输出通道=16）
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1) # 卷积层2（输入=16，输出=32）
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)       # 2x2 池化层
        self.fc1 = nn.Linear(32 * 7 * 7, 128)        # 全连接层1
        self.fc2 = nn.Linear(128, 10)      # 输出层（10 类）

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # 卷积1 -> ReLU -> 池化
        x = self.pool(torch.relu(self.conv2(x)))  # 卷积2 -> ReLU -> 池化
        x = x.view(-1, 32 * 7 * 7)                # Flatten,展平 (32 * 7 * 7) -> (batch_size, 1568)
        x = torch.relu(self.fc1(x))  # 全连接层1
        x = self.fc2(x)  # 输出层
        return x
#
# # 训练 CNN
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN().to(device)

criterion = nn.CrossEntropyLoss()                                       # 交叉熵损失（分类任务）
optimizer = optim.Adam(model.parameters(), lr=0.001)                    # Adam优化器,model.parameters()获取所有可训练参数
# scheduler = StepLR(optimizer, step_size=10, gamma=0.1)                  # 每 10 轮学习率减少 10 倍

epochs = 5
for epoch in range(epochs):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        # 前向传播
        outputs = model(images)
        loss = criterion(outputs, labels)


        # 反向传播 & 更新参数
        optimizer.zero_grad()                                           # 清空梯度
        loss.backward()                                                 # 计算梯度
        optimizer.step()                                                # 更新梯度
        # scheduler.step()                                                # 更新学习率

    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# 训练完成
print("\n训练完成！")
torch.save(model.state_dict(), "cnn_mnist.pth")
print("模型已保存为 cnn_mnist.pth")

# 模型测试
model = CNN()
model.load_state_dict(torch.load("cnn_mnist.pth"))
model.to(device)
image, label = test_dataset[0]  # 取第一张图片
image = image.unsqueeze(0).to(device)  # 添加 batch 维度，并移动到 GPU

# 进行推理
model.eval()
with torch.no_grad():
    output = model(image)
    _, predicted = torch.max(output, 1)

# 显示图片
plt.imshow(image.cpu().squeeze(), cmap="gray")
plt.title(f"预测结果: {predicted.item()} (真实: {label})")
plt.show()
