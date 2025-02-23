from cell import Cell
from node import Node
from time import sleep
import random
import os


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = None
        self._seed = seed
        if seed is None:
            random_data = os.urandom(8)
            self._seed = int.from_bytes(random_data, byteorder="big")
        random.seed(self._seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        

    def _create_cells(self):
        self._cells = [[Cell(self.win) for x in range(self.num_rows)] for i in range(self.num_cols)]
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + (self.cell_size_x * i)
        y1 = self.y1 + (self.cell_size_y * j)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(25)

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0:
            return
        last_x = len(self._cells) - 1
        last_y = len(self._cells[last_x]) - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[last_x][last_y].has_bottom_wall = False
        self._draw_cell(last_x, last_y)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            not_visited = []
            left = (i - 1 if i > 0 else None, j)
            right = (i + 1 if i < len(self._cells) - 1 else None, j)
            top = (i, j - 1 if j > 0 else None)
            bottom = (i, j + 1 if j < len(self._cells[i]) - 1 else None)
            directions = [left, right, top, bottom]
            for d in directions:
                if None in d:
                    continue
                if not self._cells[d[0]][d[1]].visited:
                    not_visited.append(d)
            if len(not_visited) == 0:
                self._draw_cell(i, j)
                return
            direction = random.choice(not_visited)
            not_visited.remove(direction)
            if direction == left:
                self._cells[i][j].has_left_wall = False
                self._cells[direction[0]][direction[1]].has_right_wall = False
            elif direction == right:
                self._cells[i][j].has_right_wall = False
                self._cells[direction[0]][direction[1]].has_left_wall = False
            elif direction == top:
                self._cells[i][j].has_top_wall = False
                self._cells[direction[0]][direction[1]].has_bottom_wall = False
            elif direction == bottom:
                self._cells[i][j].has_bottom_wall = False
                self._cells[direction[0]][direction[1]].has_top_wall = False
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for r in self._cells:
            for cell in r:
                cell.visited = False

    def _animate(self, speed=1):
        if self.win is None:
            return
        self.win.redraw()
        if speed > 0:
            sleep(0.05 / speed)

    def solve(self, algorithm="depth_first"):
        if algorithm == "depth_first":
            return self._solve_r(0,0)
        elif algorithm == "a_star":
            return self._solve_a_star_r(0,0)

    def _solve_r(self, i, j):
        self._animate(5)
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[-1]) - 1:
            return True
        left = (i - 1 if i > 0 else None, j)
        right = (i + 1 if i < len(self._cells) - 1 else None, j)
        top = (i, j - 1 if j > 0 else None)
        bottom = (i, j + 1 if j < len(self._cells[i]) - 1 else None)
        directions = [left, right, top, bottom]
        for d in directions:
            if None in d:
                continue
            if self._cells[d[0]][d[1]]:
                if self._cells[d[0]][d[1]].visited:
                    continue
                if d == left and self._cells[i][j].has_left_wall:
                    continue
                if d == right and self._cells[i][j].has_right_wall:
                    continue
                if d == top and self._cells[i][j].has_top_wall:
                    continue
                if d == bottom and self._cells[i][j].has_bottom_wall:
                    continue
                self._cells[i][j].draw_move(self._cells[d[0]][d[1]])
                if self._solve_r(d[0],d[1]):
                    return True
                self._cells[i][j].draw_move(self._cells[d[0]][d[1]], undo=True)
        return False
    
    def _solve_a_star_r(self, i, j):
        start = Node(i,j)
        goal = Node(len(self._cells) - 1, len(self._cells[-1]) - 1)
        open_cells = [start]
        closed_cells = []
        while open_cells:
            open_cells.sort(key=lambda node: node.g, reverse=False)
            open_cells.sort(key=lambda node: node.f(), reverse=True)
            node_current = open_cells.pop()
            closed_cells.append(node_current)
            if node_current == goal:
                path = []
                while node_current is not None:
                    path.append(node_current)
                    node_current = node_current.parent
                path.reverse()
                for c in range(len(path)):
                    if c == 0:
                        continue
                    i = path[c-1].i
                    j = path[c-1].j
                    i2 = path[c].i
                    j2 = path[c].j
                    self._cells[i][j].draw_move(self._cells[i2][j2])
                    self._animate(5)
                return True
            i2 = node_current.i
            j2 = node_current.j
            left = (i2 - 1 if i2 > 0 else None, j2)
            right = (i2 + 1 if i2 < len(self._cells) - 1 else None, j2)
            top = (i2, j2 - 1 if j2 > 0 else None)
            bottom = (i2, j2 + 1 if j2 < len(self._cells[i2]) - 1 else None)
            directions = [left, right, top, bottom]
            neighbours = []
            for d in directions:
                if None in d:
                    continue
                if d == left and self._cells[i2][j2].has_left_wall:
                    continue
                if d == right and self._cells[i2][j2].has_right_wall:
                    continue
                if d == top and self._cells[i2][j2].has_top_wall:
                    continue
                if d == bottom and self._cells[i2][j2].has_bottom_wall:
                    continue
                neighbour = Node(d[0], d[1])
                if neighbour in open_cells:
                    neighbour = open_cells[open_cells.index(neighbour)]
                if neighbour not in closed_cells:
                    neighbours.append(neighbour)
            for node in neighbours:
                tentative_g = node_current.g + node_current.h(node)
                if node not in open_cells:
                    open_cells.append(node)
                elif tentative_g >= node.g:
                    continue
                node.parent = node_current
                node.g = tentative_g
                node.h(goal)
                self._cells[i2][j2].draw_move(self._cells[node.i][node.j], undo=True)
                self._animate(10)
        return False
                    
    def get_seed(self):
        return self._seed