import sys
from collections import deque

import Kenken as Ken


class Solver:
    def __init__(self, game: Ken):
        self.game = game
        self.stack = deque()
        # self.stack.pop()

    def check(self):
        return self.game

    def dfs(self):
        self.unk()
        while 0 in range(len(self.game.field)):
            if not self.game.victory_check():
                try:
                    i, j = self.stack[-1]
                except IndexError:
                    return False
                self.game.print_game()
                if self.number(self.game.size, i, j, self.game.field[i][j]):
                    self.unk()
                else:
                    self.stack.pop()
            else:
                break
        return self.game.field

    def unk(self):
        for row in range(0, self.game.size):
            for column in range(0, self.game.size):
                if self.game.field[row][column] == 0:
                    self.stack.append((row, column))
                    return

    def number(self, size, i, j, prev):
        for val in range(prev + 1, size + 1):
            self.game.field[i][j] = val
            if self.game.is_valid(val, i, j):
                self.game.field[i][j] = val
                self.game.print_game()
                if self.game.victory_check():
                    self.victory = True
                return True
                # if self.game.victory_check():
                #     print("VICTORY!!!")
                #     self.victory = True
                # print(self.victory)


                    # Bad choice, make it blank and check again
        self.game.field[i][j] = 0
        return False

    victory = False
    def bctk(self):
        size = self.game.size
        if self.victory:
            return
        for i in range(0, size):
            for j in range(0, size):
                if self.game.field[i][j] == 0:
                    for val in range(1, size+1):
                        if self.game.is_valid(val, i, j):
                            self.game.field[i][j] = val
                            if self.game.victory_check():
                                print("VICTORY!!!")
                                self.victory = True
                            self.game.print_game()
                            # print(self.victory)
                            self.bctk()

                            if not self.victory:
                                # Bad choice, make it blank and check again
                                self.game.field[i][j] = 0
                    return


    def fwck(self):
        res = self.game.victory_check()
        return res

    def solve(self, algorithm):
        if algorithm == "DFS":
            self.dfs()
        elif algorithm == "backtracking":
            self.bctk()
        elif algorithm == "forward_check":
            self.fwck()
        else:
            sys.stderr.write("ERR: Unknown algorithm")
            return -1

