import hashlib

from constants import *
from tkinter import *


def draw_grid_colour(cnv):

    for l in range(NB_LINE):
        for c in range(NB_COLUMN):

            x1 = c * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
            y1 = l * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
            x2 = x1 + COTE_CASE
            y2 = y1 + COTE_CASE

            if (l + c) % 2 == 0:

                cnv.create_rectangle(x1, y1, x2, y2, fill=BG_1, width=0)

            else:
                cnv.create_rectangle(x1, y1, x2, y2, fill=BG_2, width=0)


def draw_with_coordo(list_coordo, colour, cnv):

    for i in list_coordo:

        (l, c) = i

        x1 = c * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
        y1 = l * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
        x2 = x1 + COTE_CASE
        y2 = y1 + COTE_CASE

        # str(color)
        cnv.create_rectangle(x1, y1, x2, y2, fill=colour, width=2)


def clear_with_coordo(coordo, cnv):

    (l, c) = coordo

    x1 = c * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
    y1 = l * (COTE_CASE + LINE_WIDTH / 2) + LINE_WIDTH / 2 + 3
    x2 = x1 + COTE_CASE
    y2 = y1 + COTE_CASE

    if (l + c) % 2 == 0:

        cnv.create_rectangle(x1, y1, x2, y2, fill='#75ff7e', width=0)

    else:
        cnv.create_rectangle(x1, y1, x2, y2, fill='#279227', width=0)


def draw_apple(coordo, cnv):

    (l, c) = coordo

    x = c * (COTE_CASE + LINE_WIDTH / 2) + (COTE_CASE + LINE_WIDTH + 3) / 2
    y = l * (COTE_CASE + LINE_WIDTH / 2) + (COTE_CASE + LINE_WIDTH + 3) / 2
    r = COTE_CASE / 2.5

    create_circle(cnv, x, y, r, fill='red')


def create_circle(cnv, x, y, r, **kwargs):
    return cnv.create_oval(x - r, y - r, x + r, y + r, **kwargs)
