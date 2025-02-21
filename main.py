from window import Window
from point import Point
from line import Line


def main():
    win = Window(800, 600)
    p1 = Point(0,0)
    p2 = Point(800, 0)
    l1 = Line(p1, p2)
    win.draw_line(l1, "red")
    p3 = Point(0,0)
    p4 = Point(0, 600)
    l2 = Line(p3, p4)
    win.draw_line(l2, "blue")
    p5 = Point(800,0)
    p6 = Point(800, 600)
    l3 = Line(p5, p6)
    win.draw_line(l3, "green")
    p7 = Point(0,600)
    p8 = Point(800, 600)
    l4 = Line(p7, p8)
    win.draw_line(l4, "purple")
    win.wait_for_close()

main()