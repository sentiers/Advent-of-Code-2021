from itertools import permutations

# 0: A B C _ E F G  |6|
# 1: _ _ C _ _ F _  |2| -unique
# 2: A _ C D E _ G  |5| 
# 3: A _ C D _ F G  |5|
# 4: _ B C D _ F _  |4| -unique
# 5: A B _ D _ F G  |5| 
# 6: A B _ D E F G  |6|
# 7: A _ C _ _ F _  |3| -unique
# 8: A B C D E F G  |7| -unique 
# 9: A B C D _ F G  |6| 

def count_1_4_7_8(outputs):
    return sum(sum(len(d) in (2, 4, 3, 7) for d in digits)for digits in outputs)

def total_outputs(inputs, outputs):
    patterns = {'ab': 1, 'acdfg': 2, 'abcdf': 3, 'abef': 4, 'bcdef': 5,
               'bcdefg': 6, 'abd': 7, 'abcdefg': 8, 'abcdef': 9,  'abcdeg': 0}
    abcdefg = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    total = 0
    for i in range(len(inputs)):
        for p in permutations(abcdefg): # 7!
            perm = {key: value for key, value in zip(p, abcdefg)}
            perm_input = ["".join(perm[char] for char in x) for x in inputs[i]]                    
            # if all elements(sorted) in input matches with pattern, calculate output
            if all("".join(sorted(perm_in)) in patterns for perm_in in perm_input):
                perm_output = ["".join(perm[char] for char in x) for x in outputs[i]]
                perm_output = ["".join(sorted(x)) for x in perm_output] # sort
                total += int("".join(str(patterns[x]) for x in perm_output))
                break
    return total

def calc():
    with open('digits.txt') as file:
        lines = file.read().splitlines()
    inputs = [line.split(" | ")[0].split(" ") for line in lines]
    outputs = [line.split(" | ")[1].split(" ") for line in lines]
    # In the output values, how many times do digits 1, 4, 7, or 8 appear?
    print('Digits 1, 4, 7, 8 appeared {} times'.format(count_1_4_7_8(outputs)))
    # What do you get if you add up all of the output values?
    print('Sum of output values is {}'.format(total_outputs(inputs, outputs)))

calc()