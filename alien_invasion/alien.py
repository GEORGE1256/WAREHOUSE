import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # 表示外星人的类
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并获取其rect 值
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人的初始位置在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        # 为啥只存储x, 而不存储Y？
        self.x = float(self.rect.x)
        
    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # 向右移动外星人
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x


# 原来是放错地方了！没有在项目文件夹中放入alien.bmp 文件

# 多次找问题都无果的情况下，就找最简单的因素。往往是最简单的因素导致了问题。