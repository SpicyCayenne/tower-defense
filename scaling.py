"""Gets the scaling info used in the other modules of the game"""
import pygame
pygame.init()
DISPLAY_INFO = pygame.display.Info()

def get_scaling_info():
    """Gathers display info for scaling elements of the game"""
    scaling_info = pygame.display.Info()
    x_ratio = DISPLAY_INFO.current_w/scaling_info.current_w
    y_ratio = DISPLAY_INFO.current_h/scaling_info.current_h
    return scaling_info, x_ratio, y_ratio
