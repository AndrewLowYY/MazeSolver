from point import Point
from line import Line

class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, point1, point2, window):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        self._win = window
        self.visited = False
    
    def draw(self):
        left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(left_line, "black")
        else:
            self._win.draw_line(left_line, "white")
        
        right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(right_line, "black")
        else:
            self._win.draw_line(right_line, "white")

        top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(top_line, "black")
        else:
            self._win.draw_line(top_line, "white")

        bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, "black")
        else:
            self._win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell, undo=False):
        colour = "red"
        if undo:
            colour = "gray"
        line = Line(Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2))
        self._win.draw_line(line, colour)


        