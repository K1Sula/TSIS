import pygame

pygame.init()

quality = (1940, 1000)
surface = pygame.display.set_mode((quality))
name_pro = pygame.display.set_caption("Circle")

white = (255,255,255)
red = (255,0,0)

center_w = quality[0] // 2
center_h = quality[1] // 2
run = True
FPS = 60
tickrate = pygame.time.Clock()

x = center_w
y = center_h

while run == True:
    surface.fill(white)

    history_press = pygame.key.get_pressed()
    if history_press[pygame.K_UP] == True and y >= 41:
        y -= 20
    if history_press[pygame.K_LEFT] == True and x >= 41:
        x -= 20
    if history_press[pygame.K_RIGHT] == True and x <= 1900:
        x += 20
    if history_press[pygame.K_DOWN] == True and y <= 950:
        y += 20

    pygame.draw.circle(surface , red, (x, y), 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()