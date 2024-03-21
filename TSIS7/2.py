import pygame

pygame.init()

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1440

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


player = pygame.Rect((100, 50, 100 ,50))

run_time = True
while run_time == True:

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(8 ,6)
        
    pygame.draw.rect(screen, (255, 145, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_time = False

    pygame.display.update()

pygame.quit()
