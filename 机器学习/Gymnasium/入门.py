import gymnasium as gym

# 创建环境，这里直接用gym自带的冰壶场景
env = gym.make("FrozenLake-v1", is_slippery=False)

# space 合法的数据（可以看到什么？可以做什么？）
print("观察空间：", env.observation_space)
print("动作空间：", env.action_space)

# sample() : 随机生成一个合法值
action = env.action_space.sample()
# contains() : 检查一个值是否合法
print(env.action_space.contains(action))  # True


# 搭建空间
import numpy as np
from gymnasium import spaces

# Box 空间 (更紧凑的表示当前体力,离食物距离)
observation_space = spaces.Box(
    low=np.array([0,0], dtype=np.float32),
    high=np.array([100,50], dtype=np.float32),
    dtype=np.float32
)

# Dict 空间 （有结构的表示）
observation_space = spaces.Dict({
    "energy": spaces.Box(0,100, shape=(1,), dtype=np.float32),
    "food_distance": spaces.Box(0,50, shape=(1,), dtype=np.float32),
})

