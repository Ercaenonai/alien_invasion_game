#bullet class
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #class to manage bullets fired from ship
    
    def __init__(self, ai_game):
        #create bullet obj. at ship's position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #create bullet rect, then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #store position as a decimal
        self.y = float(self.rect.y)
    
    #move bullet up the screen
    def update(self):
        #update decimal position of bullet
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y = self.y
        
    #draw bullet on screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)