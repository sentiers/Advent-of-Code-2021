import numpy as np

def probe(x_vel, y_vel, x_min, x_max, y_min, y_max):
    x_pos, y_pos = 0, 0 # start position
    y_pos_max = 1
    isTarget = False
    while (x_pos < x_max and y_pos > y_min) and not isTarget:
        x_pos += x_vel
        x_vel -= np.sign(x_vel)  # due to drag, 0 if x==0, 1 if x > 0
        y_pos += y_vel
        y_vel -= 1  # due to gravity
        y_pos_max = max(y_pos_max, y_pos)
        isTarget = x_min <= x_pos <= x_max and y_min <= y_pos <= y_max
    return isTarget, y_pos_max

def calc():
    with open('input.txt') as file:
        data = [x.split("=")[1] for x in file.read().split(",")]
        x_min, x_max = [int(x) for x in data[0].split("..")]
        y_min, y_max = [int(x) for x in data[1].split("..")]
    highest_y = 0
    count_vel_val = 0
    for x_vel in range(x_max+1):
        for y_vel in range(y_min, 2*abs(y_max)):
            isTarget, y_pos_max = probe(x_vel, y_vel, x_min, x_max, y_min, y_max)
            if isTarget:
                highest_y = max(highest_y, y_pos_max)
                count_vel_val += 1
    # What is the highest y position it reaches on this trajectory?
    print('Highest y position: {}'.format(highest_y))
    # How many distinct initial velocity values?
    print('Values count: {}'.format(count_vel_val))


calc()
