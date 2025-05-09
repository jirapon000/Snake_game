import pygame
import time
import random

pygame.init()

# Window setup
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game 🐍')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (213, 50, 80)
green = (0, 255, 0)
blue  = (50, 153, 213)

# Game clock and font
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

# Snake and food size
block = 20
speed = 10

def score_display(score):
    value = score_font.render(f"Score: {score}", True, black)
    win.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            win.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        win.fill(blue)
        pygame.draw.rect(win, green, [foodx, foody, block, block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block, snake_list)
        score_display(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
