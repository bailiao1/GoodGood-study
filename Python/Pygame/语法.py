pygame.init()                                                          # 环境初始化

pygame.display.set_caption("str")                                      # 设置标题


# 创建游戏时钟
clock = pygame.time.Clock()
clock.tick(n)                                                          # 控制每秒生成的帧数(放在循环内) rt = clock.tick(n) 可获取每帧的时长
clock.get_fps()	                                                       # 获取实际运行时的帧率（float）监视帧率

# 场景初始化
screen = pygame.display.set_mode((m,n))                                # 设置场景(窗口)大小，screen是自定义的窗口对象，pygame.FULLSCREEN 则可以自适应全屏
screen.fill(color)                                                     # 清空画面并填充背景颜色，通常放在while内第一行执行

# 处理事件（监听键鼠点按）
for event in pygame.event.get():
    if event.type == pygame.QUIT:                                      # 如果当前是QUIT(点击右上x) 
        running = False                                                # running为False，关闭运行
    elif event.type == pygame.KEYDOWN:                                 # 键盘类
        if event.key == pygame.K_SPACE:                                # 如果按到空格(pygame.K_SPACE)
            jump()                                                     # 执行函数

# 处理持续状态（长按）
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:                                                # < 键
    player_x -= speed                                                  # x坐标 向左移动 

pygame.display.flip()                                                  # 执行，运行到这一步画面才会出现，和 fill 刷新屏幕 对应
pygame.quit()                                                          # 结束，释放内存(一般放在循环外，或绑定pygame.QUIT)


# 文字显示
font = pygame.font.SysFont(name, size, bold=False, italic=False)       # 设置字体(字体名称（默认为None），大小，是否加粗，是否斜体）
text_surface = font.render("你好，世界", True, (255, 255, 255))         #  文字 （要显示的文字，是否抗锯齿，文字颜色）
screen.blit(text_surface, (100, 100))                                  # 渲染，把文字画上去（文字，坐标）


# 碰撞箱
pygame.draw.rect(screen,color,rect,线宽)	                               # 在 screen 上画 color 色的 rect(矩形), 线宽可设定，用于查看贴图角色的显示碰撞边界，为2的话，箱子为空心
pygame.draw.circle()	                                               # 画圆
pygame.draw.line()	                                                   # 画直线
pygame.draw.polygon()	                                               # 画多边形
pygame.draw.ellipse()	                                               # 画椭圆

# 碰撞激活
if xxx.colliderect(xx):                                                # 如果xxx碰到了xx，执行下面代码

    
# 坐标
pos = pygame.Vector(2,1)                                               # 在(2,1)坐标创建一个点对象            # 代替了x，y分别建立，整合player_x,player_y
pos += pygame.Vector(2,0)                                              # 移动点对象，向右两格                 # 但还是可以使用 pos.x 和 pos.y 获取x,y的具体值            

# 计算两点距离
distance = (p1 - p2).length()                                          # 前提 p1 和 p2 是点对象 
# 获取单位方向向量
(target - origin).normalize()	                                       
                                         

# 贴图
screen.blit(image, rect)                                                




