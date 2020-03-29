"""Homebrew tower defense game using pygame and object oriented programming.
This is a learning project"""
import pygame
from tower import Tower
from scaling import get_scaling_info

get_scaling_info()

def run_game():
    """Runs the game"""
    pygame.init()
    get_scaling_info()
    width, height = get_scaling_info()[1:]
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32)
    pygame.display.set_caption("Tower Defense")
    game_surface = screen.copy()

    def toggle_fullscreen():
        """Toggles between fullscreen and windowed mode"""
        if screen.get_flags() & pygame.FULLSCREEN:
            return pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        return pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    def update_display():
        """Update the game display"""
        scaling_info = get_scaling_info()[0]
        screen.fill((0, 0, 0))
        for tower in Tower.towers:
            tower.draw()
        screen.blit(pygame.transform.scale(
            game_surface, (scaling_info.current_w, scaling_info.current_h)), (0, 0))
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
                if event.key == pygame.K_F11:
                    toggle_fullscreen()
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    tower_type = Tower.selection_dict[event.key]
            if event.type == pygame.MOUSEBUTTONDOWN and tower_type != 0:
                #to prevent game from breaking if no tower selected.
                mouse_x, mouse_y = pygame.mouse.get_pos()
                Tower(tower_type, mouse_x, mouse_y, game_surface).create_tower()

        update_display()

    pygame.quit()

run_game()
