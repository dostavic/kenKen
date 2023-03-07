import sys
from collections import deque

import pygame

import Kenken as Ken
import display


class SolverGUI:
    def __init__(self, game: Ken):
        self.game = game
        self.stack = deque()
        self.display = display.Display(game)
        run = True
        select_maps_check = False
        pygame.display.update()
        while run:
            pygame.display.update()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if keys[pygame.K_1]:
                    self.dfs(0, 0)
                    break
                if keys[pygame.K_2]:
                    self.bctk()
                if keys[pygame.K_3]:
                    self.fwck()
                if keys[pygame.K_4]:
                    select_maps_check = True
                    self.game = self.select_map(0)
                    while select_maps_check:
                        keys = pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                select_maps_check = False
                            if keys[pygame.K_1]:
                                select_maps_check = False
                                self.game = self.select_map(3)
                            if keys[pygame.K_2]:
                                select_maps_check = False
                                self.game = self.select_map(4)
                            if keys[pygame.K_3]:
                                select_maps_check = False
                                self.game = self.select_map(5)
                            if keys[pygame.K_4]:
                                select_maps_check = False
                                self.game = self.select_map(8)
                            if keys[pygame.K_5]:
                                select_maps_check = False
                                self.game = self.select_map(9)

        pygame.quit()


    def select_map(self, number_map):
        self.display.draw_maps_select()
        pygame.display.update()

        if number_map != 0:
            str_map = "kenken" + str(number_map) + ".txt"

            with open(str_map, 'r') as f:
                size = int(f.readline())
                lines = f.readlines()[0:]
            f.close()

            self.game = Ken.KenKen(size, lines)
            self.display = display.Display(self.game)
        return self.game

    def dfs(self, row, col):
        self.display.draw()
        # pygame.display.update()
        pygame.display.flip()

        # pygame.time.wait(100)

        if self.game.check_row_column() and self.game.victory_check():
            print("SOLVE")
            return True

        for row in range(row, self.game.size):
            for col in range(col, self.game.size):

                # print(row, col)
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
        self.display.draw()
        # pygame.display.update()
        pygame.display.flip()
        # pygame.time.wait(100)

        # pygame.time.wait(10000000)

        size = self.game.size
        if self.victory:
            return
        for i in range(0, size):
            for j in range(0, size):
                if self.game.field[i][j] == 0:
                    for val in range(1, size + 1):
                        if self.game.is_valid(val, i, j):
                            self.game.field[i][j] = val
                            if self.game.victory_check():
                                print("VICTORY!!!")
                                self.victory = True
                            # self.game.print_game()
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
        self.display.draw()
        # pygame.display.update()
        pygame.display.flip()
        # pygame.time.wait(100)

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
                                print("VICTORY!!!")
                                self.victory = True
                            # self.game.print_game()
                            self.fwck()

                            if not self.victory:
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
