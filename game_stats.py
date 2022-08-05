#game stats
class GameStats:
    
    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        #high score never reset
        self.high_score = 0
        
    def reset_stats(self):
        #initialize stats that change during game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1