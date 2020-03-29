"""Homebrew tower defense game using pygame and object oriented programming.
This is a learning project"""
import os
import pygame
from tower import Tower

def run_game():
    """Runs the game"""
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Tower Defense")

    background = pygame.Surface(screen.get_size()).convert()
    background = pygame.image.load(os.path.join('assets', 'levels', 'level0_bg.png'))

    def update_display():
        """Update the game display"""
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for tower in Tower.towers:
            tower.draw()
        pygame.display.update()

    run = True
    tower_type = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    tower_type = Tower.selection_dict[event.key]
            if event.type == pygame.MOUSEBUTTONDOWN and tower_type != 0:
                #to prevent game from breaking if no tower selected.
                mouse_x, mouse_y = pygame.mouse.get_pos()
                Tower(tower_type, mouse_x, mouse_y, screen).create_tower()

        update_display()

    pygame.quit()

run_game()
