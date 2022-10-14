import curses
from curses import wrapper
from time import sleep
from random import randint
#test

def main(screen):
    row = 0
    col = 0
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    while True:
        try:
            digit = randint(0, 1)
            screen.addstr(str(digit), curses.color_pair(1) | curses.A_BOLD)
            col = col + 1
            row = row + 1

        except:
            sleep(0.5)
            screen.refresh()
            screen.clear()
            pass
    pass


wrapper(main)
