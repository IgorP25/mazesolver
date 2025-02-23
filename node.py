from math import sqrt


class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.g = 0
        self._h = 0
        self.parent = None

    def distance(self, other):
        return abs(self.i - other.i) + abs(self.j - other.j)
    
    def h(self, goal):
        self._h = self.distance(goal)
        return self._h
    
    def f(self):
        return self.g + self._h
    
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j
    