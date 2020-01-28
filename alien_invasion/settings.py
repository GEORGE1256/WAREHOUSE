class Settings():
    """存储设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3


        # 子弹的设置
        # self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        # self.alien_speed_factor = 1
        self.fleet_drop_factor = 10
        # 1 = 向右移；-1 = 向左移;表示 2 个意思：移动方向、移动步长；
        # 如果用Ture OR false, 则无法表示
        # self.fleet_direction = 1

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 动态设置(集中管理可变的值)；嵌套函数
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 2

        # 1 = 向右移；-1 = 向左移;表示 2 个意思：移动方向、移动步长；
        # 如果用Ture OR false, 则无法表示
        self.fleet_direction = 1

        # 计分：一个外星人 = 50 分；
        self.alien_points = 50

    def increase_speed(self):
        # 提高速度的设置
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        # 提高得分速度
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)；没打击完一次外星人编组之后，分值增加一次

"""
代码有两种布置方式：
1. 按照对象布置：如ship 是根据ship 这个对象的操作，放在一起，方便调用和搜索，类似的还有 aliens.py, bullets.py

2. 根据代码功能布置：比如settings，收集的所有的配置项目，好处是可以快速的调整配置，不需要在各个对象文件中寻找

3. 每个文件内部，再根据一定规则分类：比如settings.py文件中，根据设置功能、使用节点、类型分类，将增加速度
    的设置单独封装（increase_speed()）。

以上两种方法，第一种更常见、普遍，第二种较少。

总之，一切都是为了更好的理解、调整。

"""




