# 导入python 库、模块
# import sys
import pygame
# 导入其他文件
from pygame.sprite import Group
from settings import Settings
from ship import Ship
# from alien import Alien 导入Alien 类
from game_stats import GameStats
from button import Button
# 导入其他文件；重命名
import game_functions as gf

def run_game():
    # 初始化游戏；创建屏幕对象；
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )    
    pygame.display.set_caption("Alien Invasion")
    # 创建Play 按钮
    play_button = Button(ai_settings, screen, "Play (p)")
    
    # 创建存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建飞船；一个子弹编组；一个外星人编组
    ship = Ship(ai_settings, screen)
    # 创建存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 创建外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始主循环
    while True: 

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 判断是否处于活动状态
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 重新绘制屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
            

run_game()

