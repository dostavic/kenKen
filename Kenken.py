import copy
import re
import sys


class KenKen:

    def __init__(self, size, lines):
        self.field = [[0 for i in range(size)] for j in range(size)]
        self.blocks = list()

        self.size = size
        self.lines = lines
        for l in lines:
            var, op, val = l.split()
            self.blocks.append([[int(x) for x in re.findall('\d', var)], op, int(val)])

    # Valides input. if there are same numbers in row or col returns False
    def is_valid(self, n, x, y):

        if (x < 0 or x >= self.size) or (y < 0 or y >= self.size):
            # sys.stderr.write("ERR: Invalid coordinates")
            return False

        if n <= 0 or n > 9:
            # sys.stderr.write("ERR: Invalid number")
            return False

        for i in range(len(self.field)):
            if self.field[x][i] == n and i != y:
                # sys.stderr.write("ERR: This number already is in this row")
                return False
            if self.field[i][y] == n and i != x:
                # sys.stderr.write("ERR: This number already is in this column")
                return False

        # self.field[x][y] = n
        return self.validate_blocks()

    # input number without validation
    def input(self, n, x, y):
        if (x < 0 or x >= self.size) or (y < 0 or y >= self.size):
            sys.stderr.write("ERR: Invalid coordinates")
            return False

        self.field[x][y] = n
        return True

    def check_row_column(self):
        # print("SDJKSDAKKSAJD")
        # self.print_game()
        field_t = copy.deepcopy(self.field)
        field_b = copy.deepcopy(self.field)
        # self.print_game()
        for i in range(self.size):
            for j in range(self.size):
                field_t[i][j] = field_t[j][i]



        for i in field_b:
            arr = i
            s_arr = set(arr)
            if len(arr) != len(s_arr):
                return False

        for i in field_t:
            arr = i
            s_arr = set(arr)
            if len(arr) != len(s_arr):
                return False
        return True

    def victory_check(self):

        for block in self.blocks:
            if block[-2] == "add":
                res = 0
                for i in range(0, len(block[0]), 2):
                    res += self.field[block[0][i + 1]][block[0][i]]
                if res != block[-1]:
                    return False
            elif block[-2] == "sub":
                res = 0
                for i in range(0, len(block[0]), 2):
                    res = abs(res)
                    res -= self.field[block[0][i + 1]][block[0][i]]
                if abs(res) != block[-1]:
                    return False
            elif block[-2] == "mult":
                res = 1
                for i in range(0, len(block[0]), 2):
                    res *= self.field[block[0][i + 1]][block[0][i]]
                if res != block[-1]:
                    return False
            elif block[-2] == "div":
                nums = []
                not_complete_block = False
                for i in range(0, len(block[0]), 2):
                    if self.field[block[0][i + 1]][block[0][i]] == 0:
                        not_complete_block = True
                    nums.append(self.field[block[0][i + 1]][block[0][i]])
                if not_complete_block:
                    continue

                nums.sort(reverse=True)
                res = nums[0] / nums[1]

                if res != block[-1]:
                    return False
        return True

    def validate_blocks(self):

        for block in self.blocks:
            if block[-2] == "add":
                res = 0
                not_complete_block = False
                for i in range(0, len(block[0]), 2):
                    if self.field[block[0][i + 1]][block[0][i]] == 0:
                        not_complete_block = True
                        break
                    res += self.field[block[0][i + 1]][block[0][i]]

                if not_complete_block:
                    continue

                if res != block[-1]:
                    return False
            elif block[-2] == "sub":
                res = 0
                not_complete_block = False

                for i in range(0, len(block[0]), 2):
                    if self.field[block[0][i + 1]][block[0][i]] == 0:
                        not_complete_block = True
                    res = abs(res)
                    res -= self.field[block[0][i + 1]][block[0][i]]

                if not_complete_block:
                    continue

                if abs(res) != block[-1]:
                    return False
            elif block[-2] == "mult":
                res = 1
                not_complete_block = False

                for i in range(0, len(block[0]), 2):
                    if self.field[block[0][i + 1]][block[0][i]] == 0:
                        not_complete_block = True
                    res *= self.field[block[0][i + 1]][block[0][i]]

                if not_complete_block:
                    continue

                if res != block[-1]:
                    return False
            elif block[-2] == "div":
                nums = []
                not_complete_block = False
                for i in range(0, len(block[0]), 2):
                    if self.field[block[0][i + 1]][block[0][i]] == 0:
                        not_complete_block = True
                    nums.append(self.field[block[0][i + 1]][block[0][i]])
                if not_complete_block:
                    continue

                nums.sort(reverse=True)
                res = nums[0] / nums[1]

                if res != block[-1]:
                    return False
        return True


    def full_print(self):
        for i in self.blocks:
            print(i)

        print("------------BLOCKS-------------")

        xcords = []
        for i in range(len(self.field)):
            xcords.append(i)
        print("X:", str(xcords))
        print("--------------------------------------")
        for i in range(len(self.field)):
            print(f"{i}:", self.field[i])

    def print_game(self):
        xcords = []
        for i in range(len(self.field)):
            xcords.append(i)
        print("X:", str(xcords))
        print("------------------------------")
        for i in range(len(self.field)):
            print(f"{i}:", self.field[i])
        print("=========================")

    # Only for check
    def fill_array(self, size):
        # arr = [[1, 5, 4, 2, 3], [3, 1, 5, 4, 2], [2, 3, 1, 5, 4], [5, 4, 2, 3, 1], [4, 2, 3, 1, 5]]
        arr = [[2, 1, 3], [1, 3, 2], [3, 2, 1]]
        for i in range(size):
            for j in range(size):
                self.field[i][j] = arr[i][j]

