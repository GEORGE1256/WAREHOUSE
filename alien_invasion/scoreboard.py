import pygame.font

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

    def show_score(self):
        # 显示得分
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)







