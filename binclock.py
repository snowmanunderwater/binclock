from datetime import datetime
from time import sleep

cur_time = str(datetime.now().strftime('%H:%M:%S'))

clock = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

def rotated_cw(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def rotated_ccw(array_2d):
    list_of_tuples = zip(*array_2d[::1])
    return [list(elem) for elem in list_of_tuples]

rotated_clock = rotated_cw(clock)


for x, row in enumerate(rotated_clock):
    for y, element in enumerate(row):
        if cur_time[x] == '0':
            rotated_clock[x] = [0, 0, 0, 0]
        if cur_time[x] == '1':
            rotated_clock[x] = [0, 0, 0, 1]
        if cur_time[x] == '2':
            rotated_clock[x] = [0, 0, 1, 0]
        if cur_time[x] == '3':
            rotated_clock[x] = [0, 0, 1, 1]
        if cur_time[x] == '4':
            rotated_clock[x] = [0, 1, 0, 0]
        if cur_time[x] == '5':
            rotated_clock[x] = [0, 1, 0, 1]
        if cur_time[x] == '6':
            rotated_clock[x] = [0, 1, 1, 0]
        if cur_time[x] == '7':
            rotated_clock[x] = [0, 1, 1, 1]
        if cur_time[x] == '8':
            rotated_clock[x] = [1, 0, 0, 0]
        if cur_time[x] == '9':
            rotated_clock[x] = [1, 0, 0, 1]

def draw_clock(clock):
    for row in clock:
        for element in row:
            if element == 0:
                print('\x1b[0;30;40m|\x1b[0m', end='')
            else:
                print('\x1b[1;31;40m|\x1b[0m', end='')
        print()
    print('\x1b[0;33;40m%s\x1b[0m' % (cur_time))

draw_clock(rotated_ccw(rotated_clock))
