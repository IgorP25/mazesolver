from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    m1 = Maze(10, 10, 19, 26, 30, 30, win)
    if not m1.solve():
        print("Maze cannot be solved. Try again.")
    win.wait_for_close()

main()