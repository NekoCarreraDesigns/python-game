# import modules
import pygame
import random

# pygame initialize
pygame.init()

# global screen variable
screen = pygame.display.set_mode((800, 600))

# caption and title for game
pygame.display.set_caption("Pimpin ain't easy")
captionImg = pygame.image.load('space-ship.png')
pygame.display.set_icon(captionImg)

# Player image
playerImg = pygame.image.load('space.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image
enemyImg = pygame.image.load('alien-one.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0

# extra enemies to add later, potentially need their own functions
# enemyImg1 = pygame.image.load('alien-ship.png')
# enemy1X = random.randint(0, 800)
# enemy1Y = random.randint(50, 150)
# enemy1X_change = 0

# enemyImg2 = pygame.image.load('alien.png')
# enemy2X = random.randint(0, 800)
# enemy2Y = random.randint(50, 150)
# enemy2X_change = 0

# player function to diplay player


def player(x, y):
    screen.blit(playerImg, (x, y))

# enemy function to display enemy


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# function to create game window


def draw_window(screen):
    pass


# game loop
run = True
while run:

    screen.fill((0, 0, 0))
# player in game functions, movement and exit, as well as function calls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
