class GameStats():
    # 跟踪游戏统计信息

    def __init__(self, ai_settings):
        # 初始化游戏统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 游戏刚启动时，处于非活跃状态
        self.game_active = False

    def reset_stats(self):
        
        self.ships_left = self.ai_settings.ship_limit



"""
1. 拼写错误：ai_settings
"""