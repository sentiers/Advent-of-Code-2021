from collections import Counter

def fish_after_days(fishes, days):
    fish_count = Counter(fishes)    
    for _ in range(days):
        zero = 0 # store zero value       
        for time in range(8):
            if time == 0: 
                zero = fish_count[time]
            fish_count[time] = fish_count[time + 1] # decrement
        fish_count[6] += zero # 0 to 6
        fish_count[8] = zero # add 8
    return sum(fish_count.values())

def calculate():
    with open('fish.txt') as file:
        fishes = list(map(int, file.read().split(',')))   
    # How many lanternfish would there be after 80 days and 256 days?
    print('after 80 days: {} fishes'.format(fish_after_days(fishes, 80)))
    print('after 256 days: {} fishes'.format(fish_after_days(fishes, 256)))

calculate()