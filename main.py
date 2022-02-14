import pygame
import random

pygame.font.init()
pygame.init()

screen_width = 800
screen_height = 800
play_width = 700
play_height = 600

top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

win = pygame.display.set_mode((screen_width, screen_height))
hos = 20
track = 0


class Game(object):
    def __init__(self, hos, track):
        self.hos = hos
        self.track = track


def draw_screen(surface):
    surface.fill((0, 0, 0))
    pygame.font.init()
    font = pygame.font.SysFont("Times", 60)
    label = font.render("Pimpin ain't easy", 1, (255, 255, 255))
    pygame.draw.rect(surface, (0, 0, 0), (top_left_x,
                     top_left_y, play_height, play_width))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width()/2),
                 top_left_y + play_height/2 - label.get_height()/2))
    pygame.display.update()


draw_screen(win)
pygame.display.update()
