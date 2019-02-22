import curses
import random
import time
from datetime import datetime


def max_dimensions(window):
    height, width = window.getmaxyx()
    return height, width


def draw_clock(clock, cur_time, window):
    height, width = max_dimensions(window)
    height, width = height-8, width-8

    window.attrset(curses.color_pair(1))

    for x, row in enumerate(clock):
        for y, char in enumerate(row):
            if char == 0:
                window.addch(x+int(height/2), y+int(width/2), ' ')
            else:
                window.addch(x+int(height/2), y+int(width/2), '|')

    window.attrset(curses.color_pair(0))

    for x, char in enumerate(cur_time):
        window.addch(4+int(height/2), x+int(width/2), char)


def rotated_ccw(clock):
    """
    Rotate 2d_array(clock).

    [0, 0, 0, 0]    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0] => [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0]    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0]    [0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    
    """
    list_of_tuples = zip(*clock[::1])
    return [list(elem) for elem in list_of_tuples]


def main(window):
    curses.init_color(curses.COLOR_RED, 1000, 1000, 0)
    curses.init_pair(1, curses.COLOR_RED, 0)
    curses.curs_set(0)

    while True:
        window.clear()

        clock = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        cur_time = str(datetime.now().strftime('%H:%M:%S'))

        for x, row in enumerate(clock):
            for y, element in enumerate(row):
                if cur_time[x] == '0':
                    clock[x] = [0, 0, 0, 0]
                if cur_time[x] == '1':
                    clock[x] = [0, 0, 0, 1]
                if cur_time[x] == '2':
                    clock[x] = [0, 0, 1, 0]
                if cur_time[x] == '3':
                    clock[x] = [0, 0, 1, 1]
                if cur_time[x] == '4':
                    clock[x] = [0, 1, 0, 0]
                if cur_time[x] == '5':
                    clock[x] = [0, 1, 0, 1]
                if cur_time[x] == '6':
                    clock[x] = [0, 1, 1, 0]
                if cur_time[x] == '7':
                    clock[x] = [0, 1, 1, 1]
                if cur_time[x] == '8':
                    clock[x] = [1, 0, 0, 0]
                if cur_time[x] == '9':
                    clock[x] = [1, 0, 0, 1]

        clock = rotated_ccw(clock)

        draw_clock(clock, cur_time, window)
        window.refresh()
        time.sleep(0.05)


if __name__ == '__main__':
    curses.wrapper(main)
