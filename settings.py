#game settings class
class Settings:
    #class to store all settings for game
    
    def __init__(self):
        #initialize game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        #ship speed setting
        self.ship_speed = 1.5
        
        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction 1 is right -1 is left
        self.fleet_direction = 1

        self.ship_limit = 3