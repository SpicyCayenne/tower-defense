"""Homebrew tower defense game using pygame and object oriented programming.
This is a learning project"""
import math
import os
import random
import pygame
import level
from level import Level
from player import PLAYER
from tower import Defender, create_elf_tower, create_dwarf_tower
from enemy import Hostile
from projectiles import Projectile

#coords = [] #this is used for quickly getting coordinates


def run_game():
    """Runs the game"""
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Tower Defense")

    spawn_creep = 26
    elf_tower_attack = 27
    dwarf_tower_attack = 28
    pygame.time.set_timer(elf_tower_attack, 800)
    pygame.time.set_timer(dwarf_tower_attack, 2500)
    pygame.time.set_timer(spawn_creep, 1000)

    level_count = 0
    current_level = "LEVEL_" + str(level_count)
    this_level = getattr(level, current_level)

    background = pygame.Surface(screen.get_size()).convert()
    bg_file = this_level.load()[0]
    background = pygame.image.load(os.path.join(bg_file))

    score_font = lives_font = pygame.font.Font('freesansbold.ttf', 32)
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    def update_display():
        """Update the game display"""
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        this_level.draw_towers(screen)
        for tower in Defender.towers:
            tower.draw()
        for enemy in Hostile.enemies:
            enemy.draw()
        for ammo in Projectile.fired:
            ammo.draw()
        show_score(10, 10)
        show_lives(650, 10)
        if PLAYER.lives <= 0:
            game_over()
        pygame.display.update()

    def show_score(score_x, score_y):
        score = score_font.render("Score: " + str(PLAYER.score), True, (255, 255, 255))
        screen.blit(score, (score_x, score_y))

    def show_lives(lives_x, lives_y):
        lives_text = lives_font.render("Lives: " + str(PLAYER.lives), True, (255, 0, 0))
        screen.blit(lives_text, (lives_x, lives_y))

    def game_over():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 250))
        for enemy in Hostile.enemies:
            enemy.speed = 0

    run = True
    tower_type = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == elf_tower_attack:
                for tower in Defender.towers:
                    if tower.tower_type == "elf":
                        tower.attack()
            if event.type == dwarf_tower_attack:
                for tower in Defender.towers:
                    if tower.tower_type == "dwarf":
                        tower.attack()
                if random.randrange(0, 100) < this_level.spawn_rate and this_level.enemy_count > 0:
                    Hostile('goblin.png', Hostile.path[0][0], Hostile.path[0][1],
                            0.25, 100, screen).spawn()
                    this_level.enemy_count -= 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE and this_level.enemy_count > 0:
                    Hostile('goblin.png', Hostile.path[0][0], Hostile.path[0][1],
                            0.25, 100, screen).spawn()
                    this_level.enemy_count -= 1
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    tower_type = Defender.selection_dict[event.key]
            if event.type == pygame.MOUSEBUTTONDOWN and tower_type != 0:
                #to prevent game from breaking if no tower selected.
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for loc in Level.tower_coords:
                    distance = math.sqrt((mouse_x - loc[0])**2 + (mouse_y - loc[1])**2)
                    if distance <= 20:
                        if tower_type == "elf":
                            create_elf_tower(loc[0], loc[1], screen)
                        elif tower_type == "dwarf":
                            create_dwarf_tower(loc[0], loc[1], screen)
                        #Defender(tower_type, loc[0], loc[1], 100, screen).create_tower()
            elif event.type == pygame.MOUSEBUTTONDOWN and tower_type == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #coords.append((mouse_x, mouse_y))
        for enemy in Hostile.enemies:
            enemy.move()
        for projectile in Projectile.fired:
            projectile.move()
            projectile.collision()
        update_display()
    pygame.quit()
    #print(coords)
run_game()
