from copy import deepcopy
from time import time

solved_sudokus = []


class Grid:
    def __init__(self):
        self.nodes = [0] * 81

    def appendNode(self, value, position):
        if 0 <= position < 81:
            self.nodes[position] = value
        else:
            raise

    def nodeInfo(self, position):
        if 0 <= position < 81:

            col_number = position % 9
            row_number = position // 9
            box_number = 0

            if position % 9 < 3:
                if position // 9 < 3:
                    box_number = 0
                elif 3 <= position // 9 < 6:
                    box_number = 3
                else:
                    box_number = 6
            elif 3 <= position % 9 < 6:
                if position // 9 < 3:
                    box_number = 1
                elif 3 <= position // 9 < 6:
                    box_number = 4
                else:
                    box_number = 7
            else:
                if position // 9 < 3:
                    box_number = 2
                elif 3 <= position // 9 < 6:
                    box_number = 5
                else:
                    box_number = 8

            return (row_number, col_number, box_number)

        else:
            raise

    def findRow(self, position):
        rows = [[j + i * 9 for j in range(9)] for i in range(9)]
        return [self.nodes[i] for i in rows[self.nodeInfo(position)[0]]]

    def findCol(self, position):
        cols = [[j * 9 + i for j in range(9)] for i in range(9)]
        return [self.nodes[i] for i in cols[self.nodeInfo(position)[1]]]

    def findBox(self, position):
        boxes = [[] for i in range(9)]
        for i in range(81):

            if i % 9 < 3:
                if i // 9 < 3:
                    boxes[0].append(i)
                elif 3 <= i // 9 < 6:
                    boxes[3].append(i)
                else:
                    boxes[6].append(i)
            elif 3 <= i % 9 < 6:
                if i // 9 < 3:
                    boxes[1].append(i)
                elif 3 <= i // 9 < 6:
                    boxes[4].append(i)
                else:
                    boxes[7].append(i)
            else:
                if i // 9 < 3:
                    boxes[2].append(i)
                elif 3 <= i // 9 < 6:
                    boxes[5].append(i)
                else:
                    boxes[8].append(i)

        return [self.nodes[i] for i in boxes[self.nodeInfo(position)[2]]]

    def printGrid(self):
        grid = ""

        for i in range(9):
            for j in range(9):
                grid += str(self.nodes[i * 9 + j])
            grid += "\n"
        print(grid)

    def isSolved(self):
        if 0 in self.nodes:
            return False
        return True


def txtReader(path):
    with open(path, "r") as raw_data:
        return raw_data.readlines()


def tryToSolve(grid):
    while True:
        any_change = False
        for i in range(81):
            candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            if grid.nodes[i] == 0:
                for j in grid.findRow(i):
                    candidates.discard(j)
                for j in grid.findCol(i):
                    candidates.discard(j)
                for j in grid.findBox(i):
                    candidates.discard(j)
                if len(candidates) == 1:
                    grid.appendNode(candidates.pop(), i)
                    any_change = True
                elif len(candidates) == 0:
                    return "error"
        if not any_change:
            break

    if grid.isSolved():
        global solved_sudokus
        solved_sudokus.append(grid)
        return True
    else:
        return False


def trialAndError(grid):
    trial = None
    for i in range(81):
        candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        if grid.nodes[i] == 0:
            for j in grid.findRow(i):
                candidates.discard(j)
            for j in grid.findCol(i):
                candidates.discard(j)
            for j in grid.findBox(i):
                candidates.discard(j)
            if len(candidates) == 0:
                trial = "error"
            if len(candidates) == 1:
                grid.appendNode(candidates.pop(), i)
            if len(candidates) == 2 and trial != "error":
                trial = (candidates.pop(), candidates.pop(), i)

    return trial


def solveSudoku(grid):
    trial = tryToSolve(grid)
    is_solved = False

    if trial is True:
        return True

    cands = trialAndError(grid)
    if cands == "error":
        return False
    else:
        first_cand, sec_cand, pos = cands
        recovery_grid = deepcopy(grid)

    if trial is False:
        grid.appendNode(first_cand, pos)
        is_solved = solveSudoku(grid)

    if is_solved is True:
        return True

    if trial is False:
        grid = recovery_grid
        grid.appendNode(sec_cand, pos)
        is_solved = solveSudoku(grid)

    if is_solved is True:
        return True

    return False


def main():
    start_time = time()
    raw_data = txtReader("Problem 096.txt")
    grids = []
    ans = 0

    for i in range(50):
        new_grid = Grid()
        for j in range(1, 10):
            for k in range(9):
                new_grid.appendNode(int(raw_data[i * 10 + j][k]), k + (j - 1) * 9)

        grids.append(new_grid)

    for grid in grids:
        solveSudoku(grid)

    global solved_sudokus
    for grid in solved_sudokus:
        ans += int("".join(list(map(str, grid.nodes[0:3]))))

    print(ans)
    end_time = time()
    print(end_time-start_time)


main()

# answer: 24702
# 28.08.2020