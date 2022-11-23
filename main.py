from affichage import *
# from generation import *
from constante import *

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

snake = [(4, 6), (4, 5), (4, 4), (4, 3)]

direction = [game.RIGHT]

draw_grid_colour(cnv, grid)

draw_with_coordo(snake, 5, cnv)

generate_button = Button(window, text="Play", font='Helvetica 15 bold',
                         background='light gray')

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=2 * TAB_GAP)

verify_button = Button(window, text="Simulate", font='Helvetica 15 bold',
                         background='light gray')

verify_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=3 * TAB_GAP)

window.bind("<Left>", lambda event: game.go_left(direction))
window.bind("<Up>", lambda event: game.go_up(direction))
window.bind("<Right>", lambda event: game.go_right(direction))
window.bind("<Down>", lambda event: game.go_down(direction))

game.move_the_snake(window, cnv, snake, direction)

window.mainloop()






