import pygame.font
# P258

class Button():

    def __init__(self, ai_settings, screen, msg):
        # 初始化按钮属性
        # 获得screen_rect 值
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使按钮居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 创建按钮标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # 将msg渲染为图像，并在按钮上居中
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        # self.rect.center == 按钮的中心
        # self.msg_image_rect.center: 表示文字的中心
        # 原理：文字的中心 = 按钮的中心

    def draw_button(self):
        # 绘制按钮、文字
        self.screen.fill(self.button_color, self.rect)
        # 在区域内填充颜色，所以用fill;
        # 在某个地方，绘制图片；
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # 语法：图片， 图片位置



        

