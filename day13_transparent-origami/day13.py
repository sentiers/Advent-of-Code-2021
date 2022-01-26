import numpy as np

def fold_paper(paper, axis, cord):
    if axis == 'x':
        half_1 = np.array(paper[:cord,:])
        half_2 = np.flipud(paper[cord+1:,:]) # flip array up-down direction
    if axis == 'y':
        half_1 = np.array(paper[:,:cord])
        half_2 = np.fliplr(paper[:,cord+1:]) # flip array left-right direction
    return np.array(half_1+half_2) # add them together as paper folds

def calc():
    with open("input.txt") as file:
        lines, folds = file.read().split('\n\n')
        x_data = [int(line.split(",")[0]) for line in lines.splitlines()]
        y_data = [int(line.split(",")[1]) for line in lines.splitlines()]
        fold_data = [fold.split(" ")[2] for fold in folds.splitlines()]
    paper = np.zeros((max(x_data)+1, max(y_data)+1))
    for x, y in zip(x_data, y_data):
        paper[x,y] = 1
    for count, fold in enumerate(fold_data):
        axis, cord = fold.split("=")
        paper = fold_paper(paper, axis, int(cord))
        # How many dots are visible on your transparent paper?
        print('{} dots after {} fold'.format((paper >= 1).sum(), count+1))
    # What code do you use to activate the infrared thermal imaging camera system?
    paper_result = np.where(paper<1,' ','#').transpose() # change to '#'
    for line in paper_result:
        print("".join([str(x) for x in line]))

calc()
