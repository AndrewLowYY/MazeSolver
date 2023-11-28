from tkinter import Tk, BOTH, Canvas
from maze import Maze

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 20, 25, 10, 10, win)
    win.wait_for_close()

main()