import torch
import torch.nn as nn

# 训练CNN来识别手写数字


# 数据加载（MNIST）
transform = transforms.Compose([                          # transforms.Compose 建立数据设置流水线
    transforms.ToTensor(),                                # 转换为 PyTorch Tensor
    transforms.Normalize((0.5,), (0.5,))                  # 归一化
])

train_dataset = torchvision.datasets.MNIST(root="./data", train=True, transform=transform, download=True)          # 下载训练集到"./data" ，transform=transform流水线为流水线
test_dataset = torchvision.datasets.MNIST(root="./data", train=False, transform=transform, download=True)          # 下载测试集到"./data" ，train=False

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)                             # 导入数据集shuffle打乱顺序，提高泛化，batch_size=64（批量为64，一次导入64份数据）
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)                              # 测试就不需要打乱了，保持稳定性

# 定义 CNN 网络
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)                        # 卷积层1（输入通道=1，输出通道=16）
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)                       # 卷积层2（输入=16，输出=32）
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)                              # 2x2 池化层
        self.fc1 = nn.Linear(32 * 7 * 7, 128)                                          # 全连接层1
        self.fc2 = nn.Linear(128, 10)                                                  # 输出层（10 类）

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))      # 卷积1 -> ReLU -> 池化
        x = self.pool(torch.relu(self.conv2(x)))      # 卷积2 -> ReLU -> 池化
        x = x.view(-1, 32 * 7 * 7)                    # Flatten,展平 (32 * 7 * 7) -> (batch_size, 1568)
        x = torch.relu(self.fc1(x))                   # 全连接层1
        x = self.fc2(x)                               # 输出层
        return x

# 训练 CNN
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN().to(device)

criterion = nn.CrossEntropyLoss()                                       # 交叉熵损失（分类任务）
optimizer = optim.Adam(model.parameters(), lr=0.001)                    # Adam优化器,model.parameters()获取所有可训练参数
# scheduler = StepLR(optimizer, step_size=10, gamma=0.1)                # 每 10 轮学习率减少 10 倍，但有时候步骤多了，反而效果变差......

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
        # scheduler.step()                                              # 更新学习率

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
