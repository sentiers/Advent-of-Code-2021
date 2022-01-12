class Board:
    def __init__(self, grid):
        self.grid = grid # list of lines of bingo data
        self.rows = len(grid) # 5
        self.cols = len(grid[0]) # 5
        self.marked = [[False for i in range(self.cols)] for i in range(self.rows)]

    def mark_number(self, number):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == number:
                    self.marked[row][col] = True # change to True

    def has_won(self): # return bool type
        return any(
            all(self.marked[row][col] for col in range(self.cols))
            for row in range(self.rows) # check rows
        ) or any(
            all(self.marked[row][col] for row in range(self.rows))
            for col in range(self.cols) # check cols
        )

    def sum_unmarked(self):
        result = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.marked[row][col]:
                    result += self.grid[row][col]
        return result

def bingo():
    with open("bingo.txt") as file:
        data = file.read().splitlines()
    numbers = data[0].split(",") # get the numbers data   
    boards = [] # get the boards data   
    for i in range(1, len(data), 6):
        lines = data[i + 1 : i + 6] # raw lines for one board
        grid = [[int(x) for x in line.split()] for line in lines] # list of lines
        boards.append(Board(grid)) # create board
    
    boards_won = [False for _ in range(len(boards))] # win board record
    first_winner = True
    # game start
    for number in numbers:
        for i, board in enumerate(boards):
            board.mark_number(int(number))
            if board.has_won():
                boards_won[i] = True
                # What will your final score be if you choose that board?
                if first_winner: # first winner
                    print('first winner score: {}'.format(board.sum_unmarked() * int(number)))
                    first_winner = False             
            # Once it wins, what would its final score be?
            if all(boards_won): # last winner
                print('last winner score: {}'.format(board.sum_unmarked() * int(number)))
                exit()

bingo()