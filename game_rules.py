import random

from constante import *
from tkinter import *
import affichage
import time

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4


VIDE = 0
APPLE = 1


def move_the_snake(window, cnv, snake, grid, count, compteur_lbl, direction):

    l, c = snake[0]
    # print(direction)

    # Snake mouvement

    # direction = keyBoard()

    if direction[0] == RIGHT:
        c += 1
    elif direction[0] == LEFT:
        c -= 1
    elif direction[0] == UP:
        l -= 1
    elif direction[0] == DOWN:
        l += 1

    # direction to determine

    # TODO : bfs to determine direction

    # continue mouvement




    snake.insert(0, (l, c))
    # print(snake[0])

    # Snake display

    affichage.draw_with_coordo([snake[0]], 'yellow', cnv)
    affichage.clear_with_coordo(snake[-1], cnv)



    if not stop_game(snake):


        # eat apple 
        if grid[l][c] == APPLE:
            count += 1
            print(count)
            grid[l][c] = VIDE

            compteur_lbl['text'] = str(count)

            tps1 = time.time()
            spawn_apple(grid, snake, cnv)
            tps2 = time.time()
            print("time = ", tps2 - tps1)

        else:
            # advance
            snake.remove(snake[-1])
        
        window.after(300, lambda: move_the_snake(window, cnv, snake, grid, count, compteur_lbl, direction))

    else:

        affichage.draw_with_coordo(snake, 'blue', cnv)


# Rules

def spawn_apple(grid, snake, cnv):

    rand_l = random.randint(0, NB_LINE - 1)
    rand_c = random.randint(0, NB_COLUMN - 1)

    while (rand_l, rand_c) in snake:
        rand_l = random.randint(0, NB_LINE - 1)
        rand_c = random.randint(0, NB_COLUMN - 1)

    grid[rand_l][rand_c] = APPLE
    affichage.draw_apple((rand_l, rand_c), cnv)


def stop_game(snake):

    l, c = snake[0]

    if l >= NB_LINE or l < 0:
        return True
    elif c >= NB_COLUMN or c < 0:
        return True

    for i in range(1, len(snake)):
        if (l, c) == snake[i]:
            return True
    return False


# Mouvement

def go_left(direction):

    if direction[0] != RIGHT:
        direction[0] = LEFT


def go_right(direction):

    if direction[0] != LEFT:
        direction[0] = RIGHT


def go_up(direction):

    if direction[0] != DOWN:
        direction[0] = UP


def go_down(direction):

    if direction[0] != UP:
        direction[0] = DOWN


# Start game


