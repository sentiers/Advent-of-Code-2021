import numpy as np

def risk_levels(data_p):
    result = 0
    for x in range(1, data_p.shape[0] - 1):
        for y in range(1, data_p.shape[1] - 1):
            middle, up, down, left, right = data_p[x, y], data_p[x-1, y], data_p[x+1, y], data_p[x, y-1], data_p[x, y+1]
            if middle < up and middle < down and middle < left and middle < right:
                result += middle + 1
    return result

def three_basins(data_p):
    basins = []
    for x in range(1, data_p.shape[0] - 1):
        for y in range(1, data_p.shape[1] - 1):
            basins.append(basin(x, y, data_p))
    basins.sort(reverse=True)  # sorting
    return basins[0]*basins[1]*basins[2]

def basin(x, y, data_p):  # recursive
    result = 0
    middle, up, down, left, right = data_p[x, y], data_p[x-1, y], data_p[x+1, y], data_p[x, y-1], data_p[x, y+1]
    if middle != 9: # if middle is not 9, add 1 to result and change the middle value to 9
        result += 1
        data_p[x, y] = 9
    if up != 9: # if up is not 9, go up
        result += basin(x-1, y, data_p)
    if down != 9: # if down is not 9, go down
        result += basin(x+1, y, data_p)
    if left != 9: # if left is not 9, go left
        result += basin(x, y-1, data_p)
    if right != 9: # if right is not 9, go right
        result += basin(x, y+1, data_p)
    return result


def calc():
    with open('input.txt') as file:
        lines = file.read().splitlines()
    data = np.array([list(line) for line in lines], dtype=np.int32)
    data_p = np.pad(data, ((1, 1), (1, 1)), 'constant', constant_values=9)
    # What is the sum of the risk levels of all low points?
    print('Sum of the risk levels of all low points is {} '.format(
        risk_levels(data_p)))
    # multiply together the sizes of the three largest basins?
    print('Product of three largest basins is {} '.format(three_basins(data_p)))


calc()
