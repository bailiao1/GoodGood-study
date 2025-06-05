import pygame
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque


class SnakeEnv:                                                         # 环境类
    def __init__(self, width=480, height=480, block_size=20):
        self.width = width                                              # 场景宽度
        self.height = height                                            # 场景高度
        self.block_size = block_size                                    # 方块大小
        self.reset()                                                    # 创建环境实例时，自动初始化
        self.display = None                                             # 游戏窗口

    def reset(self):                                                    # 初始化环境
        self.direction = (1, 0)  # 初始向右
        self.head = (self.width//2, self.height//2)                     # 开局出生位置固定为场景中心
        self.snake = [self.head,
                      (self.head[0]-self.block_size, self.head[1]),     # 身体段，与head水平，同y坐标
                      (self.head[0]-2*self.block_size, self.head[1])]   # 尾巴同理
        self.score = 0                                                  # 初始化score
        self.food = self.spawn_food()                                   # 生成food
        self.frame = 0                                                  # 步数(帧)初始化
        return self.get_state()                                         # 输出当前状态

    def spawn_food(self):
        while True:
            x = random.randrange(0, self.width, self.block_size)   # 随机在范围内以 block_size 的步长生成 food 坐标
            y = random.randrange(0, self.height, self.block_size)
            if (x, y) not in self.snake:                                # 且保证不与蛇发生重叠
                return (x, y)

    def step(self, action):                                             # 获取下一步 action 更新游戏状态
        self.frame += 1                                                 # 步数+1
        self.move(action)                                               # 执行 action

        reward = 0                                                      # 初始化本轮得分
        done = False                                                    # 初始化结束判定

        if self.is_collision(self.head):                                # 判断是否死亡，如果为True，本局结束且扣分(负反馈)
            done = True
            reward = -10
            return self.get_state(), reward, done, {}

        self.snake.insert(0, self.head)                          # 没触发done，正常执行游戏逻辑，重新插入头，更新位置

        if self.head == self.food:                                      # 如果吃到food，reward 正反馈，游戏得分+1
            reward = 10
            self.score += 1
            self.food = self.spawn_food()                               # 重新生成食物坐标,且本轮不删除尾巴，长度+1
        else:
            self.snake.pop()                                            # pop删除尾巴，蛇前进

        reward += 0.1                                                   # 活着每步也给一点鼓励
        return self.get_state(), reward, done, {}                       # 返回本轮状态

    def is_collision(self, point):                                      # 获取head坐标，判断是否死亡
        x, y = point
        if x < 0 or x >= self.width or y < 0 or y >= self.height:       # 如果坐标越界(撞墙)
            return True                                                 # 返回True，step中执行done流程
        if point in self.snake[1:]:                                     # 检测到蛇咬到自己，同理
            return True
        return False                                                    # 否则返回False,不执行done

    def move(self, action):                                                 # 执行位移
        x_dir, y_dir = self.direction                                       # direction初始值为 (1,0) 即x+1，向右移动
        directions = [(x_dir, y_dir),   # 0:直走                             # (1,0) 继续向右直行
                      (-y_dir, x_dir),  # 1:左转                             # (0,1) 停止向右，向下走(图形坐标系下，y轴是反的,所以初始向右状态下左转会变向下，右转变向上)
                      (y_dir, -x_dir)]  # 2:右转                             # (0,-1) y-1，head向上
        self.direction = directions[action]                                 # 选择执行的direction
        self.head = (self.snake[0][0] + self.direction[0]*self.block_size,  # 更新head位置
                     self.snake[0][1] + self.direction[1]*self.block_size)

    def get_state(self):                                                # 获取当前游戏状态
        head = self.snake[0]                                            # 蛇头位置
        point_l = (head[0] + -self.direction[1]*self.block_size,        # 列出下步行动的位置预设
                   head[1] + self.direction[0]*self.block_size)
        point_r = (head[0] + self.direction[1]*self.block_size,
                   head[1] + -self.direction[0]*self.block_size)
        point_s = (head[0] + self.direction[0]*self.block_size,
                   head[1] + self.direction[1]*self.block_size)

        danger = [                                                      # 判断是否会死亡
            self.is_collision(point_s),  # 前
            self.is_collision(point_r),  # 右
            self.is_collision(point_l)   # 左
        ]

        food_dx = np.sign(self.food[0] - head[0])                       # 粗略计算食物的相对方向(只是方向信息，不是距离)
        food_dy = np.sign(self.food[1] - head[1])

        dir_features = [                                                # 判断蛇的当前朝向，只有一个为1(True)，其余为0(False)
            int(self.direction == (0, -1)),  # 上
            int(self.direction == (0, 1)),   # 下
            int(self.direction == (-1, 0)),  # 左
            int(self.direction == (1, 0)),   # 右
        ]

        state = np.array(danger + [food_dx, food_dy] + dir_features, dtype=np.float32)      # 拼接所有状态组成向量(总共9维:3个danger，2个食物方向，4个朝向)
        return state                                                                        # 给神经网络作为输入

    def render(self):                                                                       # 画游戏(可视化接口)
        if self.display is None:                                                            # 如果场景未创建，初始化窗口(只做一次)
            pygame.init()
            self.display = pygame.display.set_mode((self.width, self.height))
        self.display.fill((0,0,0))                                                          # 清屏，初始化新帧

        for pos in self.snake:                                                              # 画蛇
            pygame.draw.rect(self.display, (0,255,0), pygame.Rect(pos[0], pos[1], self.block_size, self.block_size))
        pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.food[0], self.food[1], self.block_size, self.block_size))    # 画食物
        pygame.display.flip()                                                               # 更新画面(出帧)



class DQN(nn.Module):                                                                       # pytorch搭建简单的神经网络
    def __init__(self, input_size=9, output_size=3):                                        # 明确输入9维，输出3维
        super(DQN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 128),                                          # 第一层全连接(放大特征)
            nn.ReLU(),                                                                      # 第一次激活
            nn.Linear(128, 64),                                        # 第二次全连接(收缩)
            nn.ReLU(),                                                                      # 第二次激活
            nn.Linear(64, output_size)                                            # 第三次全连接(输出结果)
        )

    def forward(self, x):                                                                   # 前向传播
        return self.net(x)

class DQNAgent:                                                                            # 构建智能体
    def __init__(self, input_dim=9, output_dim=3, gamma=0.9, epsilon=1.0, epsilon_decay=0.995, epsilon_min=0.01,
                 lr=1e-3, batch_size=64, buffer_size=10000, device="gpu"):
        self.device = device
        self.model = DQN(input_dim, output_dim).to(device)
        self.target_model = DQN(input_dim, output_dim).to(device)
        self.update_target()

        self.memory = deque(maxlen=buffer_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.loss_fn = nn.MSELoss()
        self.batch_size = batch_size
        self.gamma = gamma

        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.output_dim = output_dim

    def update_target(self):
        self.target_model.load_state_dict(self.model.state_dict())

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.output_dim - 1)
        state_tensor = torch.tensor(state, dtype=torch.float32).to(self.device).unsqueeze(0)
        q_values = self.model(state_tensor)
        return torch.argmax(q_values).item()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train(self):
        if len(self.memory) < self.batch_size:
            return

        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        states = torch.tensor(states, dtype=torch.float32).to(self.device)
        actions = torch.tensor(actions, dtype=torch.long).to(self.device).unsqueeze(1)
        rewards = torch.tensor(rewards, dtype=torch.float32).to(self.device)
        next_states = torch.tensor(next_states, dtype=torch.float32).to(self.device)
        dones = torch.tensor(dones, dtype=torch.float32).to(self.device)

        # 当前Q值
        q_values = self.model(states).gather(1, actions).squeeze()

        # 目标Q值
        next_q_values = self.target_model(next_states).max(1)[0]
        targets = rewards + self.gamma * next_q_values * (1 - dones)

        loss = self.loss_fn(q_values, targets.detach())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # ε 衰减
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self, path):                                                       # 保存当前模型的主网络权重
        torch.save(self.model.state_dict(), path)

    def load(self, path):
        self.model.load_state_dict(torch.load(path, map_location=self.device))  # 加载网络权重
        self.update_target()                                                    # 同步目标网络
        
env = SnakeEnv()
agent = DQNAgent(input_dim=9, output_dim=3)

# 训练
best_score = 0

for episode in range(5000):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.get_action(state)
        next_state, reward, done, _ = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        agent.train()
        state = next_state
        total_reward += reward

    if episode % 20 == 0:
        agent.update_target()

        if env.score > best_score:
            best_score = env.score
            agent.save("best_model.pth")
        print(f"Episode {episode}, Score: {env.score}, Total Reward: {round(total_reward, 2)}")
