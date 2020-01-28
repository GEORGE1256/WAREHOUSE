
import pygame.font
from pygame.sprite import Group
# 用来创建飞船编组，显示剩余的ship
from ship import Ship
# 导入ship 类，显示剩余ship

class Scoreboard():
    # 得分信息的类
    def __init__(self, ai_settings, screen, stats):
        # 初始化涉及到的属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 设置字体
        self.text_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        # 当前得分
        self.prep_score()
        # 最高分
        self.prep_high_score()
        # 等级
        self.prep_level()
        # 剩余飞船
        self.prep_ships()


    def prep_score(self):
        # 将得分转换为一张渲染图像
        rounded_score = round(self.stats.score, -1)
        # round()将圆整到最近的10、100、1000等整数倍
        score_str = "{:,}".format(rounded_score)
        # 正则，添加千位分隔符；自动转换为str；
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放到屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_high_score(self):
        # 将最高分渲染为图像
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将图片放到屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
    
    def prep_level(self):
        # 将等级渲染为图像
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        # 显示剩余飞船
        self.ships = Group()
        # 创建空编组，存储飞船实例
        for ship_number in range(self.stats.ships_left):
            # 剩余N 个飞船，循环N 次，绘制N 个飞船
            ship = Ship(self.ai_settings, self.screen)
            """ 这句忘了是什么意思了，想不起来，尤其是 2 个参数
            Ship 类中，需要2 个参数，如上；"""
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            # ship是横着排列的
            self.ships.add(ship)
            # 将新飞船添加到编组中

    def show_score(self):
        # 显示得分；更新屏幕是调用
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船;参数表示绘制位置；
        self.ships.draw(self.screen)


        """
        在界面添加元素的思路：
        1. 先显示初始值：在game.stats.py 显示初始值
        2. 显示游戏过程中的值：在scoreboard.py 显示游戏过程中的值
        3. 最后屏幕更新到最新的值：self.screen.blit()；这一步可以归类到上一步
        4. 写出元素的计算逻辑：game_functins.py
        prep_level 被调用了 2 次，一次是初始化的时候，显示当前等级；另一次是游戏进行过程中（当外星人全部被消灭之后，调用一次）
        """








