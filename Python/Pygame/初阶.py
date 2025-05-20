pygame.init()                                                          # 环境初始化

pygame.display.set_caption("str")                                      # 设置标题


# 场景初始化
screen = pygame.display.set_mode((m,n))                                # 设置场景(窗口)大小，screen是自定义的窗口对象
screen.fill(color)                                                     # 清空画面并填充背景颜色，通常放在while内第一行执行

# 文字显示
font = pygame.font.SysFont(name, size, bold=False, italic=False)       # 设置字体(字体名称（默认为None），大小，是否加粗，是否斜体）
text_surface = font.render("你好，世界", True, (255, 255, 255))          #  文字 （要显示的文字，是否抗锯齿，文字颜色）
screen.blit(text_surface, (100, 100))                                  # 渲染，把文字画上去（文字，坐标）


# 碰撞箱
pygame.draw.rect(screen,color,rect,线宽)	                               # 在screen上画color色的rect,线宽可设定，用于查看贴图角色的显示碰撞边界
pygame.draw.circle()	                                               # 画圆
pygame.draw.line()	                                                   # 画直线
pygame.draw.polygon()	                                                 # 画多边形
pygame.draw.ellipse()	                                                 # 画椭圆


screen.blit(image, rect)                                               # 给对象贴图


pygame.display.flip()                                                  # 显示帧(执行了，画面才会出现，和fill对应)

pygame.quit()                                                          # 结束，释放内存


# 
xxx.colliderect(xx):                                                   # 触发判定，如果xxx碰到了xx，执行下面代码




# 处理事件
# 1. 处理事件（点按）
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            jump()

# 2. 处理持续状态（长按）
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player_x -= speed




# 创建游戏时钟
clock = pygame.time.Clock()
clock.tick(n)                                                          # 控制每秒生成的帧数
clock.get_fps()	                                                       # 获取实际运行时的帧率（float）
