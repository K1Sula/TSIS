import pygame
import random

pygame.init()

width, height = 1080, 1000

surface = pygame.display.set_mode((width, height))
road_game = pygame.image.load("image/road.png")

pygame.display.set_caption("Racer")

run = True
FPS = 60

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def rotation_image(image ,angle):
    return pygame.transform.rotate(image, angle)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("image/yellow_car.png")
        self.image = pygame.transform.scale(self.image, (100, 200))  # Resize the enemy image
        self.image = rotation_image(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0) 
 
    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width-40), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("image/blue_car.png")
        self.image = pygame.transform.scale(self.image, (100, 200))  # Resize the player image
        self.image = rotation_image(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (420, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 130:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-15, 0)
        if self.rect.right < width - 130:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(15, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
P1 = Player()
E1 = Enemy()

while run:
    tickrate = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    P1.update()
    E1.move()
    
    surface.blit(road_game,(0,0))
    P1.draw(surface)
    E1.draw(surface)
       
    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()
