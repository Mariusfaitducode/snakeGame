import random

from constants import *
from tkinter import *
import display
import time

import snakeAI




def start_game(window, cnv, snake, grid, count, compteur_lbl, direction):


    grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]
    snake = [(4, 6), (4, 5)]
    count = 0
    direction = [RIGHT]

    display.draw_grid_colour(cnv)
    display.draw_with_coordo(snake, "yellow", cnv)

    apple = (0, 0)

    spawn_apple(grid, snake, apple, cnv)
    
    # Interactions
    window.bind("<Left>", lambda event: go_left(direction))
    window.bind("<Up>", lambda event: go_up(direction))
    window.bind("<Right>", lambda event: go_right(direction))
    window.bind("<Down>", lambda event: go_down(direction))

    move_the_snake(window, cnv, snake, apple, grid, count, compteur_lbl, direction)




def start_simulation():

    pass

# Game loop

def move_the_snake(window, cnv, snake, apple, grid, count, compteur_lbl, direction):

    l, c = snake[0]
    # print(direction)

    # Snake mouvement

    snakeAI.find_best_case(snake, grid, apple, direction)

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

    display.draw_with_coordo([snake[0]], 'yellow', cnv)
    display.clear_with_coordo(snake[-1], cnv)



    if not game_over(snake):

        # eat apple 
        if grid[l][c] == APPLE:
            count += 1
            print(count)
            grid[l][c] = VIDE

            compteur_lbl['text'] = str(count)

            tps1 = time.time()
            spawn_apple(grid, snake, apple, cnv)
            tps2 = time.time()
            print("time = ", tps2 - tps1)

        else:
            # advance
            snake.remove(snake[-1])
        
        window.after(300, lambda: move_the_snake(window, cnv, snake, apple, grid, count, compteur_lbl, direction))

    else:

        display.draw_with_coordo(snake, 'blue', cnv)


# Rules

def spawn_apple(grid, snake, apple, cnv):

    rand_l = random.randint(0, NB_LINE - 1)
    rand_c = random.randint(0, NB_COLUMN - 1)

    while (rand_l, rand_c) in snake:
        rand_l = random.randint(0, NB_LINE - 1)
        rand_c = random.randint(0, NB_COLUMN - 1)

    grid[rand_l][rand_c] = APPLE

    apple = (rand_l, rand_c)

    display.draw_apple(apple, cnv)



# Verif game over
def game_over(snake):

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
        return True
    return False


def go_right(direction):

    if direction[0] != LEFT:
        direction[0] = RIGHT
        return True
    return False

def go_up(direction):

    if direction[0] != DOWN:
        direction[0] = UP
        return True
    return False


def go_down(direction):

    if direction[0] != UP:
        direction[0] = DOWN
        return True
    return False


def go_direction(dir, direction, l, c):

    valid = False
    
    if dir == RIGHT:
        valid = go_right(direction)
        c += 1

    elif dir == LEFT:
        valid = go_left(direction)
        c -= 1

    elif dir == UP:
        valid = go_up(direction)
        l -= 1

    elif dir == DOWN:
        valid = go_down(direction)
        l += 1

    return l, c, valid


# Start game


