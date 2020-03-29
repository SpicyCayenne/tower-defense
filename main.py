"""Homebrew tower defense game using pygame and object oriented programming.
This is a learning project"""
import pygame
from tower import Tower

GREEN = (150, 255, 150)
def run_game():
    """Runs the game"""
    pygame.init()

    display_info = pygame.display.Info()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 32)

    towers = []

    def toggle_fullscreen():
        """Toggles between fullscreen and windowed mode"""
        if screen.get_flags() & pygame.FULLSCREEN:
            return pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        return pygame.display.set_mode((
            display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

    def update_display():
        """Update the game display"""
        screen.fill(GREEN)
        for tower in towers:
            tower.draw()
        pygame.display.update()

    def create_tower():
        towers.append(Tower(screen, "./assets/tower.png", 400, 400))


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_F11:
                    toggle_fullscreen()
                if event.key == pygame.K_SPACE:
                    create_tower()
                    print(towers)

        update_display()

    pygame.quit()

run_game()
