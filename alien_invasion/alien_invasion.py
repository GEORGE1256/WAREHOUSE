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
from scoreboard import Scoreboard
# 导入其他文件；重命名
import game_functions as gf

def run_game(): 
    # 初始化游戏；创建屏幕对象；
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play 按钮
    play_button = Button(ai_settings, screen, "PLAY (p)")
    
    # 创建存储游戏统计信息的实例；创建记分牌
    stats = GameStats(ai_settings)
    # 此处的参数 = 初始化中的参数
    sb = Scoreboard(ai_settings, screen, stats)

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
        gf.check_events(ai_settings, screen, stats, play_button, sb, ship, aliens, bullets)
        
        # 激活游戏
        if stats.game_active:
            # 判断是否处于活动状态
            # check_events()会改变stats.game_active的值；点击“PLAY" 按钮，这个值 =True；
            ship.update()
            # ship 是一个类，
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

            """
            # 为啥bullets_update() 不放在 bullets.py文件中，而是放在了gf 中？就像ship.update() 一样
            # ship.update() 和 bullets.update() 有啥不同？如果放进去有啥缺点？
            # bullet.py中，有专门的 update() 函数；而且前者调用了后者
            这样看来，可以把update_bullets() 放入bullet.py中
            根据相同对象统一文件的原则，放入更方便阅读，更容易理解；
            """

        # 重新绘制屏幕
        # 如果放在 if 条件下，界面黑屏，无法显示
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        


run_game()

