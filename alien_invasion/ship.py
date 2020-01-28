# import os
# print("current working directory", os.getcwd())
# 以上代码用来确认当前文件的工作路径

import pygame
from pygame.sprite import Sprite
# 因为要显示剩余的ship数量，所以需要调用Sprite

class Ship(Sprite):
    # 使用sprite时，类中要传入sprite 参数

    def __init__(self, ai_settings, screen):
        # 初始化飞船；设置飞船初始位置
        # Sprite
        super(Ship, self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在ship的属性center中，存储小数值
        self.center = float(self.rect.centerx)
        # 为啥要这么做？ship 更顺畅的移动？

        """ 
        思路：
        1. 导入图像文件
        2. 获取图片、screen的rect 值
        3. 表示图片在screen 的相对位置
        """

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 移动标志，相当于一个开关；通过在其他代码中，修改移动标志的值，
        # 触发相应的代码。

    def update(self):
        # 根据移动标志，调整飞船位置
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0: 
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.settings 更新 rect 对象
        self.rect.centerx = self.center
        """在__init__代码中，有相反的写法，此处又还原了，目的是保存小数点的值；"""

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # 飞船居中
        self.center = self.screen_rect.centerx



"""
# 使用sprite时，类中要传入sprite 参数
"""
