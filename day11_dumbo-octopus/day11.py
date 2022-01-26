import numpy as np

def count_flashes(data, steps):
    count = 0
    for step in range(steps):
        flashed = []
        data += 1 # increase 1 for every octopuses
        while np.max(data)>9:
            for x in range(data.shape[0]):
                for y in range(data.shape[1]):
                    if data[x, y]>9 and (x,y) not in flashed:
                        data[x, y] = 0
                        count += 1
                        flashed.append((x,y))
                        # adjacent octopuses                                         
                        for i, j in [(1,1), (1,0), (0,1), (-1,0), (0,-1), (1,-1), (-1,1), (-1,-1)]:
                            if 0 <= x+i < data.shape[0] and 0 <= y+j < data.shape[1]: # check the boundary                           
                                if (x+i,y+j) not in flashed:
                                    data[x+i, y+j] += 1
        if is_all_flashed(flashed, data): # if all octopuses flashed, return current step
            return step + 1
    return count

def is_all_flashed(flashed, data):
    return len(flashed)==data.shape[0]*data.shape[1] 

def calc():
    with open('energy-level.txt') as file:
        lines = file.read().splitlines()
    data = np.array([list(line) for line in lines], dtype=np.int32)
    # How many total flashes are there after 100 steps?
    print('Total flashes after 100 steps: {} flashes'.format(count_flashes(data.copy(), 100)))
    # What is the first step during which all octopuses flash?
    print('When all octopuses flash: step {}'.format(count_flashes(data.copy(), 999)))

calc()

# 1603
# 222


