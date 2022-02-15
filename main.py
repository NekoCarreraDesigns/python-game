import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Pimpin ain't easy")

playerImg = pygame.image.load('space.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


def draw_window(screen):
    pass


run = True
while run:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player()
    pygame.display.update()
