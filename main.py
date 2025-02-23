from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    m1 = Maze(10, 10, 19, 26, 30, 30, win)
    m1._break_entrance_and_exit()
    m1._break_walls_r(0,0)
    m1._reset_cells_visited()
    m1.solve()
    win.wait_for_close()

main()