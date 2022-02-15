import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Pimpin ain't easy")

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480


def player():
    pass


def draw_window(screen):
    pass


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    pygame.display.update()
