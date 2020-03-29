"""Gets the scaling info used in the other modules of the game"""
import pygame
pygame.init()

def get_display_info():
    """gets the initial display info, should only be called once"""
    display_info = pygame.display.Info()
    w = display_info.current_w
    h = display_info.current_h
    return w, h, display_info

def smallest_dim():
    return min(get_display_info()[0:2])

DISPLAY = get_display_info()[2]

def get_scaling_info():
    """Gathers display info for scaling elements of the game"""
    scaling_info = pygame.display.Info()
    x_ratio = DISPLAY.current_w / scaling_info.current_w
    y_ratio = DISPLAY.current_h / scaling_info.current_h
    return scaling_info, x_ratio, y_ratio
