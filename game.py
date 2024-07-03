import random

from constants import *
import tkinter as tk
import display
import time

import snakeAI

from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Game:
    def __init__(self, window):

        # Window appearance
        self.window = window
        self.canvas = tk.Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='black')
        self.canvas.pack()
        self.canvas.place(x=TAB_GAP, y=TAB_GAP)

        display.draw_grid_colour(self.canvas)

        # Interactions
        self.window.bind("<KeyPress>", self.change_direction)

        # Game variables
        self.grid = []
        self.snake = []
        self.score = 0
        self.direction = Direction.RIGHT
        self.apple = (0, 0)

        self.game_over = False

    # Game
    def start_game(self):

        self.grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]
        self.snake = [(4, 6), (4, 5)]
        self.score = 0
        self.direction = Direction.RIGHT
        self.game_over = False

        self.spawn_apple()

        # Display game
        display.draw_grid_colour(self.canvas)
        display.draw_with_coordo(self.snake, "yellow", self.canvas)

        self.game_loop()

    def reset_game(self):

        self.canvas.delete("all")
        self.start_game()

    def game_loop(self):

        if not self.game_over:
            self.update_snake_position()
            self.check_collisions()
            self.draw_elements()
            self.window.after(500, self.game_loop)
        else:
            display.draw_with_coordo(self.snake, 'blue', self.canvas)
            self.canvas.create_text(200, 200, text="GAME OVER", fill="red", font=("Helvetica", 30))

    def draw_elements(self):
        display.draw_grid_colour(self.canvas)
        display.draw_with_coordo(self.snake, 'yellow', self.canvas)
        display.draw_apple(self.apple, self.canvas)

    # Movement Controls
    def change_direction(self, event):
        new_direction = None
        if event.keysym == "Up":
            new_direction = Direction.UP
        elif event.keysym == "Down":
            new_direction = Direction.DOWN
        elif event.keysym == "Left":
            new_direction = Direction.LEFT
        elif event.keysym == "Right":
            new_direction = Direction.RIGHT

        opposites = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }

        if new_direction and new_direction != opposites[self.direction]:
            self.direction = new_direction

    def update_snake_position(self):

        l, c = self.snake[0]

        # Snake mouvement
        # snakeAI.find_best_case(snake, grid, apple, direction)

        if self.direction == Direction.RIGHT:
            c += 1
        elif self.direction == Direction.LEFT:
            c -= 1
        elif self.direction == Direction.UP:
            l -= 1
        elif self.direction == Direction.DOWN:
            l += 1

        # display.clear_with_coordo(self.snake[-1], self.canvas)

        # self.snake = [(l, c)] + self.snake[:-1]

        self.snake.insert(0, (l, c))

        self.snake.remove(self.snake[-1])

        print(self.snake)

    # Rules
    def spawn_apple(self):

        while True:
            l = random.randint(0, NB_LINE - 1)
            c = random.randint(0, NB_COLUMN - 1)

            if (l, c) not in self.snake:
                self.grid[l][c] = APPLE
                self.apple = (l, c)
                # display.draw_apple(self.apple, self.canvas)
                return True

    def check_collisions(self):
        l, c = self.snake[0]

        # Check wall collisions
        if l >= NB_LINE or l < 0 or c >= NB_COLUMN or c < 0:
            self.game_over = True

        # Check self collisions
        # set(snake) is the list without duplicates
        if len(self.snake) != len(set(self.snake)):
            self.game_over = True

        # Check food collision
        if self.snake[0] == self.apple:
            self.snake.append(self.snake[-1])
            self.spawn_apple()
            self.update_score()

    def update_score(self):
        self.score += 1












# Verif game over



# Mouvement

# def go_left(direction):
#
#     if direction[0] != RIGHT:
#         direction[0] = LEFT
#         return True
#     return False
#
#
# def go_right(direction):
#
#     if direction[0] != LEFT:
#         direction[0] = RIGHT
#         return True
#     return False
#
# def go_up(direction):
#
#     if direction[0] != DOWN:
#         direction[0] = UP
#         return True
#     return False
#
#
# def go_down(direction):
#
#     if direction[0] != UP:
#         direction[0] = DOWN
#         return True
#     return False
#
#
# def go_direction(dir, direction, l, c):
#
#     print("dir", dir, "direction", direction, "l", l, "c", c)
#     valid = False
#
#     if dir == RIGHT:
#         print("right")
#         valid = go_right(direction)
#         c += 1
#
#     elif dir == LEFT:
#         print("left")
#         valid = go_left(direction)
#         c -= 1
#
#     elif dir == UP:
#         print("up")
#         valid = go_up(direction)
#         l -= 1
#
#     elif dir == DOWN:
#         print("down")
#         valid = go_down(direction)
#         l += 1
#
#
#     print("Validity : ", valid)
#
#     return l, c, valid


# Start game


