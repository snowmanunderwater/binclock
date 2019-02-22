from datetime import datetime
from time import sleep

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


def cook_clock(clock):
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


def draw_clock(clock):
    for row in clock:
        for element in row:
            if element == 0:
                print('\x1b[0;30;40m|\x1b[0m', end='')
            else:
                print('\x1b[1;31;40m|\x1b[0m', end='')
        print()
    print('\x1b[0;33;40m%s\x1b[0m' % (cur_time))


if __name__ == '__main__':
    cook_clock(clock)
    draw_clock(rotated_ccw(clock))
