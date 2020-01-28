class GameStats():
    # 跟踪游戏统计信息

    def __init__(self, ai_settings):
        # 初始化游戏统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 游戏刚启动时，处于非活跃状态
        self.game_active = False
        # 在任何情况下都不重置的最高分
        self.high_score = 0

    def reset_stats(self):
        
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # 每次开始，都重置，不能放在__init__中；每次点击“PLAY", 是
        # 新游戏，所以分数也要重置；
        self.level = 1



"""
1. 拼写错误：ai_settings
"""