
# How many measurements are larger than the previous measurement?
def increased():
    count = -1 # initialize count
    prev = -1 # initialize previous measurement value
    with open('depth-measure.txt') as file:
        for line in file: # loop
            if int(line) > prev:
                count += 1
            prev = int(line) # store current value to previous value
    print('increased: {}'.format(count)) # print result

# How many sums are larger than the previous sum?
def increasedSum():
    count = -1 # initialize count
    prev = -1 # initialize previous sum value
    with open('depth-measure.txt') as file:
        data = [int(i) for i in file.readlines()] # get data

    # loop from the beginning to thrid last element
    for j, depth in enumerate(data[0:-2]):
        sum = depth + data[j + 1] + data[j + 2] # calculate sum
        if sum > prev:
            count += 1
        prev = sum # store current sum to previous value  
    print('increased sum: {}'.format(count)) # print result


# run
increased()
increasedSum()