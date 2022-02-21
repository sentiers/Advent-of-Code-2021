from dataclasses import dataclass
import numpy as np

@dataclass
class Cell:
    row: int
    col: int
    risk: int

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def neighbors(self, cell): # return neighbor cells list
        neighbors = []
        row, col = cell.row, cell.col
        if row > 0:
            neighbors.append(self.grid[row - 1][col])
        if col > 0:
            neighbors.append(self.grid[row][col - 1])
        if row < self.rows - 1:
            neighbors.append(self.grid[row + 1][col])
        if col < self.cols - 1:
            neighbors.append(self.grid[row][col + 1])
        return neighbors

    def min_cost(self, start, end): # minimal cost for start cell to end cell
        cost = np.full((self.rows, self.cols), float('inf'))
        cost[start.row][start.col] = 0
        queue = [start]
        while queue:
            current = queue.pop(0) # first cell in queue
            for neighbor in self.neighbors(current):
                neighbor_cost = cost[neighbor.row][neighbor.col] 
                cost_to_neighbor = cost[current.row][current.col] + neighbor.risk
                if neighbor_cost > cost_to_neighbor:
                    cost[neighbor.row][neighbor.col] = cost_to_neighbor
                    queue.append(neighbor)
        return cost[end.row][end.col]

    def expand(self, times):
        expanded_grid = np.full((self.rows * times, self.cols * times), None)
        for row in range(self.rows * times):
            for col in range(self.cols * times):
                add = (row // self.rows) + (col // self.cols)
                risk = (self.grid[row % self.rows][col % self.cols].risk + add - 1) % 9 + 1
                expanded_grid[row][col] = Cell(row, col, risk) # fill the expanded grid
        self.__init__(expanded_grid) # reinitialize grid

def calc():
    with open('map.txt') as file:
        lines = file.read().splitlines()
        data = [[Cell(row, col, int(risk)) for col, risk in enumerate(row_data)]
                for row, row_data in enumerate(lines)]
    # what is the lowest total risk of any path from the top left to the bottom right?
    map = Grid(data)
    print('Lowest total risk in map: {}'.format(map.min_cost(map.grid[0][0], map.grid[-1][-1])))
    map.expand(5) # expand to full map
    print('Lowest total risk in full map: {}'.format(map.min_cost(map.grid[0][0], map.grid[-1][-1])))

calc()
