from Kenken import KenKen
from Solver import Solver

if __name__ == '__main__':
    with open("kenken4.txt", 'r') as f:
        size = int(f.readline())
        lines = f.readlines()[0:]
    f.close()

    game = KenKen(size, lines)
    # game.fill_array(size)

    solve = Solver(game)
    # solve.bctk()
    solve.dfs()
    # print(game.input(1, 0, 0))

    # game.print_game()
    print(game.victory_check())
