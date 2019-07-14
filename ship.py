#ship class
import pygame

class Ship:
    #class to manage ship
    
    def __init__(self, ai_game):
        #initialize the ship and set starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        #start ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store decimal for ship position
        self.x = float(self.rect.x)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        #update position based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        
        #update rect obj. from self.x
        self.rect.x = self.x
            
    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)
