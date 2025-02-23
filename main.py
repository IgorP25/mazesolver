from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    m1 = Maze(10, 10, 19, 26, 30, 30, win)
    m1.solve()
    win.wait_for_close()

main()