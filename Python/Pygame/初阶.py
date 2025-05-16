pygame.init()                                                          # 环境初始化

pygame.display.set_caption("str")                                      # 设置标题

screen = pygame.display.set_mode((m,n))                                # 设置场景(窗口)大小，screen是自定义的窗口对象
screen.fill(color)                                                     # 清空画面并填充背景颜色，通常放在while内第一行执行




pygame.quit()                                                          # 结束，释放内存


# 创建游戏时钟
clock = pygame.time.Clock()
clock.tick(n)                                                          # 控制每秒生成的帧数
clock.get_fps()	                                                       # 获取实际运行时的帧率（float）
