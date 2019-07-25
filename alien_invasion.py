#Alien INVASION!!!!!
import sys
from time import sleep
import pygame
import pygame.mixer
from pygame.mixer import Sound
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    #Class to manage game assets and behaviors
    
    def __init__(self):
        #initialize the game, and create game resources
        pygame.init()
        
        pygame.mixer.music.load('background.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)
                                     
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.bg_color = (0,0,0)
        
        self.ship = Ship(self)
        
        self.stats = GameStats(self)
        
        self.bullets = pygame.sprite.Group()
        
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        self.play_button = Button(self, "Play")
            
    def run_game(self):
        #start the main loop for the game
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets() 
                self._update_aliens()
            self._update_screen()
            
    def _check_events(self):
            #watch for keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):            
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()                    
                                    
    def _check_keyup_events(self, event):            
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                        
    def _fire_bullet(self):
        #create new bullet and add to group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            lazer = pygame.mixer.Sound('lazer.wav')
            pygame.mixer.Sound.play(lazer)
                   
    def _update_bullets(self):
        
        self.bullets.update()
        #delete bullets once off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
               
    def _check_bullet_alien_collisions(self):
        #check for bullet hit, remove bullet and alien
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        for collision in collisions:
            hit = pygame.mixer.Sound('hit.wav')
            pygame.mixer.Sound.play(hit)
            
        #destroy remaining bullets and create new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            level_up = pygame.mixer.Sound('level-up.wav')
            pygame.mixer.Sound.play(level_up)
    
    #update all aliens position in fleet
    def _update_aliens(self):
        #check if fleet at edge, then update all aliens
        self._check_fleet_edges()
        self.aliens.update()
        
        #check alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _create_fleet(self):
        #create fleet of aliens        
        alien = Alien(self)
        alien_width, alien_height  = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #determine num. rows of aliens fit on screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows):
            #create first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
            #create alien and place in row
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width +2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            
            self.aliens.add(alien)
    
    #responds to alien hitting an edge
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    #drop fleet and change direction
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    #respond to ship hit
    def _ship_hit(self):
        if self.stats.ships_left >0:
            self.stats.ships_left -= 1
            #remove remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            game_over = pygame.mixer.Sound('game over.wav')
            pygame.mixer.Sound.play(game_over)
            #create new fleet and recenter ship
            self._create_fleet()
            self.ship.center_ship()
            
            sleep(1.5)
        else:
            self.stats.game_active = False
        
    def _check_aliens_bottom(self):
        #check for aliens reaching bottom of acreen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def _update_screen(self):
            #update image on screen, flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #updates bullets on screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.aliens.draw(self.screen)
        
        #draw play button if game inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            
            #make recent display visable
        pygame.display.flip()

if __name__ == '__main__':
    #make game instance and run
    ai= AlienInvasion()
    ai.run_game()
