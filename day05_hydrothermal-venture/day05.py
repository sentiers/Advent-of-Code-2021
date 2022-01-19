import numpy as np

def add_lines(diagram, data):
    for line in data:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        x_diff, y_diff = abs(x1 - x2), abs(y1 - y2)
        if x_diff == 0: # vertical line
            for i in range(y_diff + 1):
                diagram[min(y1, y2) + i][x1] += 1            
        elif y_diff == 0:  # horizontal line
            for i in range(x_diff + 1):
                diagram[y1][min(x1, x2) + i] += 1
    return diagram

def add_d_lines(diagram, data):
    for line in data:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        x_diff, y_diff = abs(x1 - x2), abs(y1 - y2)
        if x_diff == y_diff: # diagonal line
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2): # / shape
                for i in range(x_diff + 1):
                    diagram[min(y1, y2) + i][min(x1, x2) + i] += 1
            if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2): # \ shape
                for i in range(x_diff + 1):
                    diagram[max(y1, y2) - i][min(x1, x2) + i] += 1              
    return diagram

def calc():
    rows, cols = 0, 0
    data = []
    with open("input.txt") as file:
        for line in file: # loop
            p1, p2 = line.split(" -> ")
            x1, y1 = p1.split(",")
            x2, y2 = p2.split(",")
            cols = max([int(x1), int(x2), cols]) # find the max row and col
            rows = max([int(y1), int(y2), rows])
            data.append([(int(x1), int(y1)), (int(x2), int(y2))])
    diagram = np.zeros((rows + 1, cols + 1))
    # At how many points do at least two lines overlap?
    print('overlap: {} points'.format((add_lines(diagram, data) >= 2).sum()))    
    print('overlap(+d): {} points'.format((add_d_lines(diagram, data) >= 2).sum()))   
    
calc()