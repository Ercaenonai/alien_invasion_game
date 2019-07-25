#game stats
class GameStats:
    
    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        
    def reset_stats(self):
        #initialize stats that change during game
        self.ships_left = self.settings.ship_limit