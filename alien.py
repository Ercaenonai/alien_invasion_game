#alien class
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
#class represents single alien
    
    def __init__(self, ai_game):
        #initialize alien and set starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load alien image and set its rect.
        self.image = pygame.image.load('alien2.bmp')
        self.rect = self.image.get_rect()
        
        #start each one at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
    
    #check if alien at edge of screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
       #move alien to right
    def update(self):
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
        
        

