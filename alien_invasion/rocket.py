import sys
import pygame

###思路：
# 1. 先创建一个火箭
# 2. 将火箭的初始位置放到中间
# 3. 想左移动，且不超过屏幕
# 4. 上下右移动

# 12.8 
# 飞船在屏幕左边：

def fly_rocket():
    pygame.init()
    # 画出屏幕
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Fly Rocket")
    bg_color = (230, 230, 230)

    # 画出rocket
    rocket_image = pygame.image.load('images/ship.bmp')
    # 设置图片初始化位置：在屏幕的中间
    screen_rect = screen.get_rect()
    rocket_rect = rocket_image.get_rect()

    # 将rocket放在screen 中间
    rocket_rect.centerx = screen_rect.centerx
    rocket_rect.centery = screen_rect.centery

    # 主循环：响应按键事件
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and rocket_rect.right < screen_rect.right:
                    rocket_rect.centerx += 3
                elif event.key == pygame.K_LEFT and rocket_rect.left > screen_rect.left:
                    rocket_rect.centerx -= 3
                elif event.key == pygame.K_UP and rocket_rect.top > screen_rect.top:
                    rocket_rect.centery -= 3
                elif event.key == pygame.K_DOWN and rocket_rect.bottom < screen_rect.bottom:
                    rocket_rect.centery += 3


        # 显示背景色
        screen.fill(bg_color)

        # 绘制rocket的位置
        screen.blit(rocket_image, rocket_rect)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()


# 直接写函数名称，不需要在前面添加 run
fly_rocket()


# 不用各种类、函数，也是一种挑战啊！完全按照之前的写，反而没意思

# AttributeError: 'pygame.Rect' object has no attribute 'up'

# pygame.rect pygame中Rect(left, top, width, height)的参数 用错了：
# 远点：屏幕的左上方:
# rect模块中，没有up, down 参数，只有如上四个；
# left: 距离屏幕左边的距离 
# top： 图像距离屏幕上方的距离
# width： 对象的宽度
# height： 对象的高度
# bottom: 对象的bottom距离屏幕上方的距离

#  一直按照左箭头，图片无法一直右移？