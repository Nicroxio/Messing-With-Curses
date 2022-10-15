import curses
from curses import wrapper
from math import trunc


def main(screen):
    ###Init screen size###
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    col, lin = screen.getmaxyx()
    center_col = trunc(col / 2)
    center_lin = trunc(lin / 2)
    colour1 = 2
    colour2 = 1
    colour3 = 1
    count = 1
    while True:

        screen.addstr(center_col, center_lin, "Select me", curses.color_pair(colour1) | curses.A_BOLD)
        screen.addstr(center_col + 1, center_lin, "No select me", curses.color_pair(colour2) | curses.A_BOLD)
        screen.addstr(center_col + 2, center_lin, "No NO select me", curses.color_pair(colour3) | curses.A_BOLD)
        screen.refresh()

        keypress = screen.getch()
        if str(keypress) == "259":
            count -= 1
        elif str(keypress) == "258":
            count += 1

        if count == 1:
            colour1 = 2
            colour2 = 1
            colour3 = 1
        elif count == 2:
            colour1 = 1
            colour2 = 2
            colour3 = 1
        elif count == 3:
            colour1 = 1
            colour2 = 1
            colour3 = 2
        elif count == 0:
            count = 3
            colour1 = 1
            colour2 = 1
            colour3 = 2
        else:
            count = 1
            colour1=2
            colour2=1
            colour3=1
        screen.addstr(center_col + 3, center_lin, str(count), curses.color_pair(1) | curses.A_BOLD)


if __name__ == '__main__':
    wrapper(main)
