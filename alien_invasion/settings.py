class Settings():
    """存储设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3


        # 子弹的设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_factor = 20
        # 1 = 向右移；-1 = 向左移;表示 2 个意思：移动方向、移动步长；
        # 如果用Ture OR false, 则无法表示
        self.fleet_direction = 1
