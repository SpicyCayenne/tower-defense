"""Homebrew tower defense game using pygame and object oriented programming.
This is a learning project"""
import os
import pygame
from tower import Defender
from enemy import Hostile

def run_game():
    """Runs the game"""
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Tower Defense")

    background = pygame.Surface(screen.get_size()).convert()
    background = pygame.image.load(os.path.join('assets', 'levels', 'level0_bg.png'))

    elf_tower_attack = dwarf_tower_attack = 26
    pygame.time.set_timer(elf_tower_attack, 800)
    pygame.time.set_timer(dwarf_tower_attack, 2000)

    def update_display():
        """Update the game display"""
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for tower in Defender.towers:
            tower.draw()
        for enemy in Hostile.enemies:
            enemy.draw()
        pygame.display.update()
    coord_list = []
    run = True
    tower_type = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == 26:
                for tower in Defender.towers:
                    tower.attack()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    Hostile('enemy.png', Hostile.path[0][0], Hostile.path[0][1], 0.25,
                            screen).spawn()
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    tower_type = Defender.selection_dict[event.key]
            if event.type == pygame.MOUSEBUTTONDOWN and tower_type != 0:
                #to prevent game from breaking if no tower selected.
                mouse_x, mouse_y = pygame.mouse.get_pos()
                Defender(tower_type, mouse_x, mouse_y, screen).create_tower()
            elif event.type == pygame.MOUSEBUTTONDOWN and tower_type == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                coord_list.append((mouse_x, mouse_y))
        for enemy in Hostile.enemies:
            enemy.move()
        update_display()
    print(coord_list)
    pygame.quit()

run_game()
