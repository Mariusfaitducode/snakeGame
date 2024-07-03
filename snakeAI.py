
import random
from constants import *

import game


def find_best_case(snake, grid, apple, direction):

    # rand_direction = random.randint(1, 4)

    dist = 1000

    print("Initial direction : ", direction[0])
    

    for dir in [RIGHT, LEFT, UP, DOWN]:

        copy_snake = snake

        # direction[0] = dir

        last_direction = [direction[0]]

        l, c = snake[0]

        (l, c, valid) = game.go_direction(dir, last_direction, l, c )

        # (apple_l, apple_c) = apple
        
        # vect = apple_l - l, apple_c - c

        

        # Advance snake

        if valid:
            copy_snake.insert(0, (l, c))
        
            if not game.game_over(copy_snake):

                print("Valid direction : ", last_direction[0], dir)
                direction[0] = last_direction[0]
                copy_snake.remove(snake[0])
                return
            
            else:
                print("Detect Game Over : ", last_direction[0], dir)
                copy_snake.remove(snake[0])
        else:
            print('Not valid : ', dir)

        
