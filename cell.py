from point import Point
from line import Line

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        p1 = Point(x1, y1)
        p2 = Point(x1, y2)
        l1 = Line(p1, p2)
        color = "white"
        if self.has_left_wall:
            color = "black"
        self._win.draw_line(l1, color)
        
        p1 = Point(x2, y1)
        p2 = Point(x2, y2)
        l1 = Line(p1, p2)
        color = "white"
        if self.has_right_wall:
            color = "black"
        self._win.draw_line(l1, color)
        p1 = Point(x1, y1)
        p2 = Point(x2, y1)
        l1 = Line(p1, p2)
        color = "white"
        if self.has_top_wall:
            color = "black"
        self._win.draw_line(l1, color)
        p1 = Point(x1, y2)
        p2 = Point(x2, y2)
        l1 = Line(p1, p2)
        color = "white"
        if self.has_bottom_wall:
            color = "black"
        self._win.draw_line(l1, color)

    def draw_move(self, to_cell, undo=False):
        p1 = Point(self._x1 + ((self._x2 - self._x1) / 2), self._y1 + ((self._y2 - self._y1) / 2))
        p2 = Point(to_cell._x1 + ((to_cell._x2 - to_cell._x1) / 2), to_cell._y1 + ((to_cell._y2 - to_cell._y1) / 2))
        l1 = Line(p1, p2)
        line_color = "red"
        if undo:
            line_color = "#ddd"
        self._win.draw_line(l1, line_color)
