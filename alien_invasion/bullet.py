import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 管理子弹的类

    def __init__(self, ai_settings, screen, ship):
        # 在飞船所处位置，创建子弹对象
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处，创建子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储子单位置：用小数表示
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 向上移动子弹
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹rect的为宗旨
        self.rect.y = self.y
        # 以上两个为啥不直接写成一句呢？

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)

        




# 矩形(Rectangular); 矩形结构; 矩形区域;
