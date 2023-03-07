import display
from Kenken import KenKen
from Solver import Solver
from SolverGUI import SolverGUI
import time

if __name__ == '__main__':
    with open("kenken3.txt", 'r') as f:
        size = int(f.readline())
        lines = f.readlines()[0:]
    f.close()

    game = KenKen(size, lines)
    # game.fill_array(size)

    # solve = SolverGUI(game)
    # game.fill_array()

    solve = SolverGUI(game)
    # game.full_print()
    # game.print_game()

    # display = display.Display(game)
    # display.draw_game()

    # start_time = time.time()
    # solve.dfs(0, 0)
    # solve.bctk()
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print(game.input(1, 0, 0))

    # game.fill_array(game.size)
    print("Solve")
    # game.print_game()

    # print(game.check_row_column())

    # print(game.victory_check())
