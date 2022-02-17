# import modules
import pygame
import random
import math
# pygame initialize
pygame.init()

# global screen variable
screen = pygame.display.set_mode((800, 600))

# background image for game
background = pygame.image.load('space-background.jpg')

# caption and icon for game
pygame.display.set_caption("Pimpin ain't easy")
captionImg = pygame.image.load('space-ship.png')
pygame.display.set_icon(captionImg)

# Player image
playerImg = pygame.image.load('space.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien-one.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# extra enemies to add later, potentially need their own functions
# enemyImg1 = pygame.image.load('alien-ship.png')
# enemy1X = random.randint(0, 800)
# enemy1Y = random.randint(50, 150)
# enemy1X_change = 0.3
# enemy1y_change = 40

# enemyImg2 = pygame.image.load('alien.png')
# enemy2X = random.randint(0, 800)
# enemy2Y = random.randint(50, 150)
# enemy2X_change = 0.3
# enenmy2Y_change = 40

missileImg = pygame.image.load('missile.png')
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 10
missile_state = "ready"
# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (153, 13, 55))
    screen.blit(score, (x, y))


# player function to diplay player
def player(x, y):
    screen.blit(playerImg, (x, y))

# enemy function to display enemy


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, missileX, missileY):
    distance = math.sqrt((math.pow(enemyX - missileX, 2)) +
                         (math.pow(enemyY - missileY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
run = True
while run:

    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))
# player in game functions, movement and exit, as well as function calls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if missile_state == "ready":
                    missileX = playerX
                    fire_missile(playerX, missileY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # spaceship boundary check, making sure ship stays in bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # enemy boundary check, making sure enemies stay in bounds
    enemyX += enemyX_change
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # collision detection
        collision = isCollision(enemyX[i], enemyY[i], missileX, missileY)
        if collision:
            missileY = 480
            missile_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    # missile movement
    if missileY <= 0:
        missileY = 480
        missile_state = "ready"
    if missile_state == "fire":
        fire_missile(missileX, missileY)
        missileY -= missileY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
