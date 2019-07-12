#Alien INVASION!!!!!
import sys
import pygame

class AlieanInvasion:
    #Class to manage game assets and behaviors
    
    def __init__(self):
        #initialize the game, and create game resources
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        #start the main loop for the game
        while True:
            #watch for keyboard and mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #make recent display visable
            pygame.display.flip()

if __name__ == '__main__':
    #make game instance and run
    ai= AlieanInvasion()
    ai.run_game()