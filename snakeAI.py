import math
import random
from constants import *

import game as g


def find_best_case(game):

    # rand_direction = random.randint(1, 4)



    print("Initial direction : ", game.direction)

    initial_direction = game.direction

    best_direction = None
    best_distance = 1000

    for simulate_dir in g.Direction:

        game.direction = initial_direction
        game.change_direction(simulate_dir)

        initial_snake = game.snake.copy()
        game.update_snake_position()

        if not game.verify_game_over():
            # print("Valid direction : ", game.direction, simulate_dir)
            # print("Initial snake : ", initial_snake, " - Snake : ", game.snake)

            snake_l, snake_c = game.snake[0]
            apple_l, apple_c = game.apple

            distance = math.sqrt((apple_l - snake_l) ** 2 + (apple_c - snake_c) ** 2)

            if distance < best_distance:
                best_distance = distance
                best_direction = game.direction

        # else:
            # print("Detect Game Over : ", game.direction, simulate_dir)

        game.snake = initial_snake

    if best_direction is None:
        print("No case found")
    else:
        print(best_direction)
    return best_direction

        
