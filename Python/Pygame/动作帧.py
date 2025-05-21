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
      if frame_index >= len(frames):             # 判断帧图是否播放完成
        playing = False                          # 停止播放
        frame_index = 0                          # 回归第一帧

  screen.fill((30,30,30)                         # 场景初始化
  if playing:
    screen.blit(frames[frame_index],(350,250))   # 如果处于播放状态，这一帧就播放图片
  else:
    screen.blit(frames[0],(350,250))             # 否则就渲染初始状态

  pygame.display.flip()                          # 显示
  
pygame.quit()                                    # 关闭，释放内存

# -------------------------------------------------------------------------------------------------------------------


# 简单的带碰撞箱的动画帧

def make_frame(color):                           # 创建图片的流程封装成函数
  surf = pygame.Surface((100,100))
  surf.fill(color)
  return surf

frames = [
      {"imags":make_frame((200,0,0)),"hitboxes":[]},                              # 第一帧,无碰撞
      {"imags":make_frame((0,200,0)),"hitboxes":[pygame.Rect(60,30,30,20)]},      # 第二帧,有碰撞，这里的箱子参数是(x,y,w,h) x,y是相对角色坐标，wh 则是 宽和高
      {"imags":make_frame((0,0,200)),"hitboxes":[]}                               # 第三帧,无碰撞  
      ]                                                                                          
# 小知识: 在图形中，y值变大是向下移动，且 场景screen 显示的是第四象限，即最左为0，最高为0，但负值也不会报错，只会跑出窗口

# 同样设置控制变量
frame_index = 0
frame_duration = 200
frame_time = 0
playing = False

# 创建坐标对象
player_pos = pygame.Vector2(300,300)

running = True                                          # 按流程创建主循环
while running:
  dt = clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_f:
        playing = True
        frame_index = 0
        frame_time = 0
        
  if playing:
    frame_time += dt
    if frame_time >= dt:
      frame_index += 1
      frame_time = 0
      if frame_index >= len(frames):
        playing = False
        frame_index = 0


  current_frame = frames[frame_index]                  # 创建变量获取当前帧的 图片 和 碰撞箱
  screen.fill((30,30,30))                              # 填充，刷新画面
  screen.blit(current_frame["imags"],player_pos)       # 在对应的角色坐标(player_pos) 画出当前的 动画图片，如果没做偏差，图像是现实在目标坐标的右下，图像的(0,0) 和 pos 重叠，而不是中心对齐
  
  for box in current_frame["hitboxes"]:                # 使用for循环创建当前动画的碰撞箱，且画到场景中(大多时候，箱子不止一个，这里的hit只是攻击判定箱子)
    world_box = pygame.Rect(
      player_pos.x + box.x,                              # 绑定坐标，使箱子随着角色移动
      player_pos.y + box.y,
      box.width,
      box.height
    )
    pygame.draw.rect(screen,(0,255,0),world,world_box,2) # 画箱子，线宽2：显示线框

  pygame.display.flip()                                

pygame.quit()
  


