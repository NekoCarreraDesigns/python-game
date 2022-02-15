import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))


def draw_window(surface, screen):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render(
        "Pimpin ain't easy, press any key to begin", 60, (255, 255, 255))
    surface.blit(label)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


draw_window(screen)
