from collections import Counter
from collections import defaultdict

def insert_element(string, rules, steps):
    pairs = defaultdict(int)
    # initial string
    results = Counter(string)
    for i in range(len(string)-1):
        pairs[string[i:i+2]] += 1
    # n steps
    for step in range(steps):
        new_pairs = defaultdict(int)
        for pair in pairs:
            pair_cnt = pairs[pair]
            element = rules[pair] # ex) AB -> C
            new_pairs[pair[0]+element] += pair_cnt # ex) AC
            new_pairs[element+pair[1]] += pair_cnt # ex) CB
            results[element] += pair_cnt
        pairs = new_pairs # update pairs
    return max(results.values())-min(results.values())

def calc():
    with open("input.txt") as file:
        string, rules = file.read().split('\n\n')
        rules = [(rule.split(" -> ")[0], rule.split(" -> ")[1])
                 for rule in rules.splitlines()]
    # The quantity of the most elements - the quantity of the least elements?
    print('After 10 steps: {}'.format(insert_element(string, dict(rules), 10)))
    print('After 40 steps: {}'.format(insert_element(string, dict(rules), 40)))

calc()