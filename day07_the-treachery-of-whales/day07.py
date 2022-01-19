from statistics import median, mean

def calc():
    with open('positions.txt') as file:
        positions = list(map(int, file.read().split(',')))
    fuel_median = 0
    fuel_mean = 0
    median_pos = int(median(positions)) # need median value for for set cost
    mean_pos = int(mean(positions)) # need mean value for increasing cost
    for pos in positions:
        fuel_median += abs(median_pos - pos)
        for i in range(abs(mean_pos - pos)):
            fuel_mean += i + 1
    # How much fuel must they spend to align to that position?
    print('For set cost: {} fuel'.format(fuel_median))
    print('For increasing cost: {} fuel'.format(fuel_mean))

calc()