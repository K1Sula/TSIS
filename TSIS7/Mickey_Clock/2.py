import pygame
import datetime
pygame.init()
WIDTH, HEIGHT = 1400 , 1050
surface = pygame.display.set_mode((WIDTH,HEIGHT))
Name_app = pygame.display.set_caption('Mickey Mouse Clock')
icon_app = pygame.image.load('image/mouse.png')
pygame.display.set_icon(icon_app)
foto = pygame.image.load('image/mainclock.png')
right_a = pygame.image.load('image/rightarm.png')
left_a = pygame.image.load('image/leftarm.png')
run = True
FPS = 60
tickrate = pygame.time.Clock()
center_w = WIDTH // 2
center_h = HEIGHT // 2
def rotation1(image,angel):
    return pygame.transform.rotate(image,angel)
while run:
    time = datetime.datetime.now()
    minutes = time.minute
    seconds = time.second
    angel_l = (minutes + 0.65) * 6 
    angel_r = (seconds + 8.75) * 6 
    right_hand_rotation = rotation1(right_a, -angel_r)
    left_hand_rotation = rotation1(left_a, -angel_l)
    surface.blit(foto, (0,0))
    surface.blit(right_hand_rotation, (center_w - right_hand_rotation.get_width() // 2, center_h - right_hand_rotation.get_height()// 2) )
    surface.blit(left_hand_rotation, (center_w - left_hand_rotation.get_width() // 2, center_h - left_hand_rotation.get_height()// 2) )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    tickrate.tick(FPS)
pygame.quit()