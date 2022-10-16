import curses
from curses import wrapper
from math import trunc

LIST = 5


def main(screen):
    ###Init screen size###
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    col, lin = screen.getmaxyx()
    center_col = trunc(col / 2)
    center_lin = trunc(lin / 2)
    count = 0
    count2 = count
    colours = [2]

    for i in range(LIST):
        colours.append(1)

    while True:
        for selector in range(len(colours)):
            screen.addstr(center_col + selector, center_lin, "select",
                          curses.color_pair(colours[selector]) | curses.A_BOLD)

            count2 = count

        screen.refresh()

        keypress = screen.getch()

        if str(keypress) == "259":
            count -= 1
        elif str(keypress) == "258":
            count += 1

        for selector in colours:
            if count > LIST:
                count = 0
            elif count == -1:
                count = LIST
            colours[count] = 2
            colours[count2] = 1


if __name__ == '__main__':
    wrapper(main)
