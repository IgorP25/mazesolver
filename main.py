from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    # p1 = Point(0,0)
    # p2 = Point(800, 0)
    # l1 = Line(p1, p2)
    # win.draw_line(l1, "red")
    # p3 = Point(0,0)
    # p4 = Point(0, 600)
    # l2 = Line(p3, p4)
    # win.draw_line(l2, "blue")
    # p5 = Point(800,0)
    # p6 = Point(800, 600)
    # l3 = Line(p5, p6)
    # win.draw_line(l3, "green")
    # p7 = Point(0,600)
    # p8 = Point(800, 600)
    # l4 = Line(p7, p8)
    # win.draw_line(l4, "purple")
    c1 = Cell(0, 0, 20, 20, win)
    c2 = Cell(22, 10, 42, 30, win)
    c2.has_left_wall = False
    c1.draw()
    c2.draw()
    c1.draw_move(c2)
    win.wait_for_close()

main()