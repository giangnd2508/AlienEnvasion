import sys
import pygame
from Project1 import settings
from Project1 import ship
from Project1 import alien
from Project1 import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship_1 = ship.Ship(ai_settings, screen)
    alien1 = alien.Alien(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship_1, bullets)
        ship_1.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship_1, aliens, bullets)


run_game()
