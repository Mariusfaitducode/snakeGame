from display import *
# from generation import *
from constants import *

import game_rules as game

from tkinter import *


window = Tk()
window.title("IQ Puzzler Pro")
window.geometry("1080x720")

cnv = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='black')

cnv.pack()
cnv.place(x=TAB_GAP, y=TAB_GAP)

# cnv_piece = Canvas(window, width=WIDTH_TAB, height=HEIGHT_TAB, background='light gray')

# cnv_piece.pack()
# cnv_piece.place(x=TAB_GAP, y=1 * TAB_GAP + HEIGHT_TAB)

grid = [[0 for _ in range(NB_COLUMN)] for _ in range(NB_LINE)]

snake = [(4, 6), (4, 5)]

count = 0

direction = [game.RIGHT]


# endGame = True

#  Draw boardgame

draw_grid_colour(cnv)

draw_with_coordo(snake, "yellow", cnv)

# Buttons

generate_button = Button(window, text="Play", font='Helvetica 15 bold',
                         background='light gray',  command=(lambda: game.start_game(window, cnv, snake, grid, count, compteur_lbl, direction)))

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=2 * TAB_GAP)

simulate_button = Button(window, text="Simulate", font='Helvetica 15 bold',
                       background='light gray')

simulate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=3 * TAB_GAP)


# reset_button = Button(window, text="Reset", font='Helvetica 15 bold',
#                        background='light gray', command=(lambda: reset_game(cnv, snake, grid, count, direction)))

# reset_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=4 * TAB_GAP)


# Game rules

# game.spawn_apple(grid, snake, cnv)



compteur_lbl = Label(window, text=str(count), font=("", 16))
compteur_lbl.grid(padx=8, pady=8)

# if not endGame:
#     game.move_the_snake(window, cnv, snake, grid, count, compteur_lbl, direction)


window.mainloop()


