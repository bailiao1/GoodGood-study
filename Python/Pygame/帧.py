import pygame

# 环境初始化
pygame.init()                                    # 初始化
screen = pygame.display.set_mode((960,480))      # 创建场景
clock = pygame.time.Clock()                      # 先创建时钟，下面用来获取时间，控制帧率

# 创建演示帧
frames = []                                      # 帧列表
colors = [(200,0,0),(0,200,0),(0,0,200)]         # 三个不同的颜色

for c in colors：
  surf = pygame.Surface((100, 100))              # 创建图片对象，大小为100：100
  surf.fill(c)                                   # 染色
  frames.append(surf)                            # 加入染色后的图片，总共3张不同颜色的图片

# 创建动画控制变量
frame_index = 0                                  # 当前帧的编号
frame_duration = 200                             # 每张动作帧显示200ms
frame_time = 0                                   # 帧计时，当前帧播放多久了？
playing = False                                  # 帧开关，是否要播放帧动画

# 主循环
running = True

while running:
  dt = clock.tick(60)                            # 一秒60帧，dt获取一帧的时长
  for event in pygame.event.get():
    if event.type == pygame.QUIT:                # 关闭窗口按键，不需要返回代码页终止
      running = False

    elif event.type == pygame.KEYDOWN:           # 按键类
      if event.key == pygame.K_f:                # 如果按到了 f 键
        playing = True                           # 激活播放状态
        frame_index = 0                          # 帧页初始化
        frame_time = 0                           # 时长初始化

  # 只有playing开启，才播放图片
  if playing：
    frame_time += dt
    if frame_time >= frame_duration:             # 每次加一帧时长，直到播放时长超过限制，换下一张图(动作帧)
      frame_index += 1                           # 索引改变
      frame_time = 0                             # 重新计当前图片的播放时长



  
