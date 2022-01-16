import pygame
from pygame.locals import *
from snake import Snake
from food import Food

pygame.init()

#create game window
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

#define game variable
cell_size = 10
fps = 8
clock = pygame.time.Clock()
die = False
score = 0

#define colors:
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 100)
food_color = (255, 0, 0)

#define font
font_color = (78, 81, 139)
font = pygame.font.SysFont("Constantia", 20)

#draw methods:
def draw_snake(snake):
    for body in snake:
            pygame.draw.rect(screen, body_outer, (body.x, body.y, cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (body.x+1, body.y+1, cell_size-2, cell_size-2))

def draw_food(food):
    pygame.draw.rect(screen, food_color, (food.x, food.y, cell_size, cell_size))


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def changeDir(snake, event):
    if event.key == pygame.K_UP and snake[0].dir != (0, 1):
        snake[0].dir = (0, -1)
        print("change direction to up")
    elif event.key == pygame.K_RIGHT and snake[0].dir != (-1, 0):
        snake[0].dir = (1, 0)
        print("change direction to right")
    elif event.key == pygame.K_DOWN and snake[0].dir != (0, -1):
        snake[0].dir = (0, 1)
        print("change direction to down")
    elif event.key == pygame.K_LEFT and snake[0].dir != (1, 0):
        snake[0].dir = (-1, 0)
        print("change direction to left")


def move_snake(snake):
    for i in range (len(snake)-1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y

    snake[0].move(cell_size)
    checkCollision(snake)


def checkCollision(snake):
    global die
    global score
    #hit wall
    if snake[0].x > screen_width or snake[0].x < 0 or snake[0].y > screen_height or snake[0].y < 0:
        print("You hit the wall")
        die = True

    #hit self
    for i in range (1, len(snake)):
        if snake[i].x == snake[0].x and snake[i].y == snake[0].y:
            print("you hit youself")
            die = True

    #eat food
    if snake[0].x == food.x and snake[0].y == food.y:
        print("you ate food")
        score += 1
        x = snake[-1].x
        y = snake[-1].y
        snake.append(Snake(x, y))
        food.reset()

#create snake
snake = []
snake.append(Snake(int(screen_width/2), int(screen_height/2)))


#create food
food = Food(screen_width, screen_height, cell_size)

#running game
run = True
while(run):
    clock.tick(fps)
    screen.fill(bg)
    draw_text(f"Score: {score}", font, font_color, 50, 20)
    #iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            changeDir(snake, event)

    if not die:
        move_snake(snake)

    draw_snake(snake)
    draw_food(food)

    #update display
    pygame.display.update()


pygame.quit()