from display import *
# from generation import *
from constants import *

from game import *

from tkinter import *


window = Tk()
window.title("Snake Game")
window.geometry("850x520")


game = Game(window)


# Buttons

generate_button = Button(window, text="Play", font='Helvetica 15 bold',
                         background='light gray',  command=(lambda: game.start_game()))

generate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=2 * TAB_GAP)

simulate_button = Button(window, text="Simulate", font='Helvetica 15 bold',
                       background='light gray', command=(lambda: game.start_simulation()))

simulate_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=3 * TAB_GAP)


reset_button = Button(window, text="Reset", font='Helvetica 15 bold',
                       background='light gray', command=(lambda: game.reset_game()))

reset_button.place(x=2 * TAB_GAP + WIDTH_TAB, y=4 * TAB_GAP)





# compteur_lbl = Label(window, text=str(count), font=("", 16))
# compteur_lbl.grid(padx=8, pady=8)

# if not endGame:
#     game.move_the_snake(window, cnv, snake, grid, count, compteur_lbl, direction)


window.mainloop()


