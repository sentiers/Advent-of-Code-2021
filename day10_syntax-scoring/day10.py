from collections import Counter
from statistics import median

def corrupted_error_score(corrupted_list):
    return Counter(corrupted_list)[0]*3 + Counter(corrupted_list)[1]*57 + Counter(corrupted_list)[2]*1197 + Counter(corrupted_list)[3]*25137

def calc():
    with open('input.txt') as file:
        lines = file.read().splitlines()
    inputs = [list(line) for line in lines]
    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    corrupted_list = []
    score_list = []

    for input in inputs:
        corrupted = False
        stack = []
        score = 0
        for pair in input:
            if pair in opens:
                stack.append(pair) # push to stack
            if pair in closes:
                if closes.index(pair) != opens.index(stack.pop()): # pop and check
                    corrupted_list.append(closes.index(pair))
                    corrupted = True
        if not corrupted: # if it is incomplete chunck
            while stack:
                score *= 5
                score += opens.index(stack.pop()) + 1
            score_list.append(score)
    
    # What is the total syntax error score for those errors?
    print('Syntax error score is {} '.format(corrupted_error_score(corrupted_list)))
    # What is the middle score?
    print('Middle error score for incomplete chunck is {} '.format(median(score_list)))

calc()