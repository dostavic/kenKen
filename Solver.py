import sys
from collections import deque
import Kenken as Ken


class Solver:
    def __init__(self, game: Ken):
        self.game = game
        self.stack = deque()

    def dfs(self, row, col):
        if self.game.check_row_column() and self.game.victory_check():
            return True

        for row in range(row, self.game.size):
            for col in range(col, self.game.size):
                if self.game.field[row][col] == 0:
                    for val in range(1, self.game.size + 1):
                        self.game.field[row][col] = val

                        if col + 1 < self.game.size:
                            if self.dfs(row, col + 1):
                                return True
                        else:
                            if self.dfs(row + 1, 0):
                                return True
                        self.game.field[row][col] = 0
                else:
                    if col + 1 < self.game.size:
                        if self.dfs(row, col + 1):
                            return True
                    else:
                        if self.dfs(row + 1, 0):
                            return True
                return False

    victory = False

    def bctk(self):
        size = self.game.size
        if self.victory:
            return
        for i in range(0, size):
            for j in range(0, size):
                if self.game.field[i][j] == 0:
                    for val in range(1, size + 1):
                        if self.game.is_valid(val, i, j):
                            self.game.field[i][j] = val
                            # self.game.print_game()
                            if self.game.victory_check():
                                print("VICTORY!!!")
                                self.victory = True
                            self.bctk()

                            if not self.victory:
                                # Bad choice, make it blank and check again
                                self.game.field[i][j] = 0
                    return

    # Makes range of possible numbers smaller
    # returns new list of possible number for inserting into the field
    def forward_check(self, numbers, x, y):
        for i in numbers:
            if not self.game.is_valid(i, x, y):
                numbers.remove(i)
        return numbers

    def fwck(self):
        size = self.game.size
        possible_range = list(range(1, size + 1))

        if self.victory:
            return
        for i in range(0, size):
            for j in range(0, size):
                if self.game.field[i][j] == 0:

                    possible_range = self.forward_check(possible_range, i, j)

                    for val in possible_range:
                        if self.game.is_valid(val, i, j):
                            self.game.field[i][j] = val
                            if self.game.victory_check():
                                self.victory = True
                            self.fwck()
                            if not self.victory:
                                # Bad choice, make it blank and check again
                                self.game.field[i][j] = 0
                    return

    def solve(self, algorithm):
        if algorithm == "DFS":
            self.dfs(0, 0)
        elif algorithm == "backtracking":
            self.bctk()
        elif algorithm == "forward_check":
            self.fwck()
        else:
            sys.stderr.write("ERR: Unknown algorithm")
            return -1
