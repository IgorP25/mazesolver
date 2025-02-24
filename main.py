from maze import Maze
from window import Window
import sys
from timeit import default_timer as timer

def main():
    seed = None
    algorithm = "a_star" # "a_star" | "depth_first" (default)
    num_rows = 20
    num_cols = 32
    margin = 10
    screen_x = 1920
    screen_y = 1200
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=seed)
    print(f"Seed: {m1.get_seed()}")
    start = timer()
    if not m1.solve(algorithm):
        print("Maze cannot be solved. Try again.")
    end = timer()
    print(end-start)
    win.wait_for_close()

main()
