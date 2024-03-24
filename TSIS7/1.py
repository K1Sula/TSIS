import pygame

pygame.init()

#surface  parameters
WIDTH , HEIGHT = 1000, 620
#create surface
surface = pygame.display.set_mode((WIDTH, HEIGHT)) #<- two pattern

run = True
FPS = 60
tickrate = pygame.time.Clock()



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #do surface white color
    surface.fill((255,255,255)) #<- two pattern 
    pygame.display.update()
    tickrate.tick(FPS)
    
pygame.quit()