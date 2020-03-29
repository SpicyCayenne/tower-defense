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
    game_surface = screen.copy()

    towers = []

    def toggle_fullscreen():
        """Toggles between fullscreen and windowed mode"""
        if screen.get_flags() & pygame.FULLSCREEN:
            return pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        return pygame.display.set_mode((
            display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

    def update_display():
        """Update the game display"""
        scaling_info = get_scaling_info()[0]
        screen.fill(GREEN)
        for tower in towers:
            tower.draw()
        screen.blit(pygame.transform.scale(
            game_surface, (scaling_info.current_w, scaling_info.current_h)), (0, 0))
        pygame.display.update()

    def create_tower(tower_type):
        x_scale, y_scale = get_scaling_info()[1:]
        mouse_x, mouse_y = pygame.mouse.get_pos()
        tower_image = ["./assets/", tower_type, "_tower.png"]
        tower_image_path = "".join(tower_image)
        towers.append(Tower(
            game_surface, tower_image_path, mouse_x * x_scale, mouse_y * y_scale))

    def select_tower(keypress):
        selection = {49:"elf", 50:"dwarf"}
        return selection[keypress]

    def get_scaling_info():
        scaling_info = pygame.display.Info()
        x_ratio = display_info.current_w/scaling_info.current_w
        y_ratio = display_info.current_h/scaling_info.current_h
        return scaling_info, x_ratio, y_ratio

    run = True
    tower_selection = 0
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
                    tower_selection = select_tower(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                valid_towers = ["elf", "dwarf"]
                if tower_selection in valid_towers: #to stop the game crashing if the user hasn't selected a tower yet
                    create_tower(tower_selection)

        update_display()

    pygame.quit()

run_game()
