# What do you get if you multiply your final horizontal position by your final depth?
def calc1():
    horizontal = 0
    depth = 0
    data = [(file.split(" ")[0], int(file.split(" ")[1])) for file in open("pilot.txt")]
    for (p, v) in data:
        if p == "forward":
            horizontal += v
        elif p == "up":
            depth -= v
        elif p == "down":
            depth += v
    print(depth * horizontal)

# What do you get if you multiply your final horizontal position by your final depth?
def calc2():
    horizontal = 0
    depth = 0
    aim = 0
    data = [(file.split(" ")[0], int(file.split(" ")[1])) for file in open("pilot.txt")]
    for (p, v) in data:
        if p == "forward":
            horizontal += v
            depth += aim * v
        elif p == "up":
            aim -= v
        elif p == "down":
            aim += v
    print(depth * horizontal)

# run
calc1()
calc2()