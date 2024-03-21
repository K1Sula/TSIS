import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 400, 200
WINDOW_SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Простые часы")

# Функция для отображения часов
def draw_clock():
    font = pygame.font.Font(None, 36)
    clock_running = True

    while clock_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clock_running = False

        # Получаем текущее время
        current_time = time.localtime()
        formatted_time = time.strftime("%H:%M:%S", current_time)

        # Заполняем экран белым цветом
        screen.fill(WHITE)

        # Создаем текстовую поверхность с текущим временем
        text = font.render(formatted_time, True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))

        # Отображаем текст на экране
        screen.blit(text, text_rect)

        # Обновляем экран
        pygame.display.flip()

        # Ждем одну секунду перед обновлением времени
        time.sleep(1)

    # Выход из приложения Pygame
    pygame.quit()
    sys.exit()

# Запускаем функцию для отображения часов
draw_clock()
