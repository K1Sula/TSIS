import pygame
import datetime

pygame.init()

# Surface parameters
WIDTH, HEIGHT = 1400, 1050

# Create surface
surface = pygame.display.set_mode((WIDTH, HEIGHT))

# Create name of program
name_pro = pygame.display.set_caption("Mickey Mouse Clock")

# Clock Mickey Mouse icon for app
icon = pygame.image.load('image/mouse.png')
pygame.display.set_icon(icon)

# Load image Mickey Mouse clock
foto = pygame.image.load('image/mainclock.png')

# Load right and left arm
right_a = pygame.image.load('image/rightarm.png')
left_a = pygame.image.load('image/leftarm.png')

# Important parameters of this code
run = True
FPS = 60
tickrate = pygame.time.Clock()

# Find center of foto
center_w = WIDTH // 2
center_h = HEIGHT // 2

def rotate_image(image, angle):
    """Rotate an image."""
    return pygame.transform.rotate(image, angle)

while run:
    # Get current time
    time_now = datetime.datetime.now()
    minutes = time_now.minute
    seconds = time_now.second
    
    # Calculate angles for arms
    # 1 circle 360 degree in 1 minute = 60 seconds. This mean 1 second 6 degree
    #why i do this because picture is not right and little crooked i add 1 minutes for will be right
    minute_angle = (minutes + 0.65) * 6  # 6 degrees per minute, with 9 minutes added
    #why i do this because picture is not right and little crooked i add 9 second for will be right
    second_angle = (seconds + 9) * 6  # 6 degrees per second
    
    # Rotate arms ("-" mean go clockwise)
    rotated_right_a = rotate_image(right_a, -second_angle)
    rotated_left_a = rotate_image(left_a, -minute_angle)

    # Draw on screen Mickey mouse clock
    surface.blit(foto, (0, 0))

    # Draw rotated arms
    surface.blit(rotated_right_a, (center_w - rotated_right_a.get_width() // 2, center_h - rotated_right_a.get_height() // 2))
    surface.blit(rotated_left_a, (center_w - rotated_left_a.get_width() // 2, center_h - rotated_left_a.get_height() // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    tickrate.tick(FPS)

pygame.quit()