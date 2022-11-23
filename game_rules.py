from constante import *
from tkinter import *
import affichage

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


def move_the_snake(window, cnv, snake, direction):

    x, y = snake[0]
    print(direction)

    if direction[0] == RIGHT:
        print('ok')
        y += 1
    elif direction[0] == LEFT:
        y -= 1
    elif direction[0] == UP:
        x -= 1
    elif direction[0] == DOWN:
        x += 1

    snake.insert(0, (x, y))
    print(snake[0])

    affichage.draw_with_coordo(snake, 5, cnv)
    affichage.clear_with_coordo(snake[-1], cnv)

    snake.remove(snake[-1])
    window.after(500, lambda: move_the_snake(window, cnv, snake, direction))


def stop_game():

    pass


def go_left(direction):
    print("last :", direction)
    if direction[0] != RIGHT:
        direction[0] = LEFT

    print(direction)


def go_right(direction):
    print("last :", direction)

    if direction[0] != LEFT:
        direction[0] = RIGHT

    print(direction)


def go_up(direction):
    print("last :", direction)
    if direction[0] != DOWN:
        direction[0] = UP

    print(direction)


def go_down(direction):
    print("last :", direction)
    if direction[0] != UP:
        direction[0] = DOWN

    print(direction)
