import time
import random
from cell import Cell
from point import Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve()

    def _create_cells(self):
        self._cells = []
        for i in range(0, self._num_cols):
            col = []
            for j in range(0, self._num_rows):
                cell = Cell(True, True, True, True, Point(self._x1 + (self._cell_size_x * i), self._y1 + (self._cell_size_y * j)), Point(self._x1 + (self._cell_size_x * (i + 1)), self._y1 + (self._cell_size_y * (j + 1))), self._win)
                col.append(cell)
            self._cells.append(col)

        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbours = []

            # top
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbours.append((i, j - 1))

            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbours.append((i + 1, j))

            # bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbours.append((i, j + 1))

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbours.append((i - 1, j))

            if len(neighbours) == 0:
                self._draw_cell(i, j)
                return

            
            neighbour = neighbours[random.randrange(len(neighbours))]

            # top
            if neighbour[0] == i and neighbour[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # right
            if neighbour[0] == i + 1 and neighbour[1] == j:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            # bottom
            if neighbour[0] == i and neighbour[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # left
            if neighbour[0] == i - 1 and neighbour[1] == j:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            self._break_walls_r(neighbour[0], neighbour[1])

    def _reset_cells_visited(self):
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._cells[i][j].visited = False


    def _solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # top
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            found = self._solve_r(i, j - 1)
            self._cells[i][j].draw_move(self._cells[i][j - 1], not found)
            if found:
                return True

        # right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            found = self._solve_r(i + 1, j)
            self._cells[i][j].draw_move(self._cells[i + 1][j], not found)
            if found:
                return True

        # bottom
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            found = self._solve_r(i, j + 1)
            self._cells[i][j].draw_move(self._cells[i][j + 1], not found)
            if found:
                return True

        # left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            found = self._solve_r(i - 1, j)
            self._cells[i][j].draw_move(self._cells[i - 1][j], not found)
            if found:
                return True
        
        return False