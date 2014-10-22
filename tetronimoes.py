from graphics import *

PIXELS_PER_SQUARE = 30

class Block(Rectangle):
    
    def __init__(self, point, color):
        self.point = point
        self.color = color
        self.rect = Rectangle(point, Point(point.getX() + PIXELS_PER_SQUARE, point.getY() + PIXELS_PER_SQUARE))

    def draw(self, win):
        self.rect.setFill(self.color)
        self.rect.draw(win)
        
class Shape(Block):

    def __init__(self, coords, color):
        self.blocks = []
        for coord in coords:
            self.blocks.append(Block(coord, color))

    def draw(self, win):
        for block in self.blocks:
            block.draw(win)

class I_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x - 2*PIXELS_PER_SQUARE, center.y),
                  Point(center.x - 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x , center.y),
                  Point(center.x + 1*PIXELS_PER_SQUARE, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x + 1*PIXELS_PER_SQUARE, center.y + 1*PIXELS_PER_SQUARE),
                  Point(center.x - 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x , center.y),
                  Point(center.x + 1*PIXELS_PER_SQUARE, center.y)]
        Shape.__init__(self, coords, "orange")

class L_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x - 1*PIXELS_PER_SQUARE, center.y + 1*PIXELS_PER_SQUARE),
                  Point(center.x - 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x , center.y),
                  Point(center.x + 1*PIXELS_PER_SQUARE, center.y)]
        Shape.__init__(self, coords, "cyan")

class O_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x - 1*PIXELS_PER_SQUARE, center.y + 1*PIXELS_PER_SQUARE),
                  Point(center.x - 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x, center.y),
                  Point(center.x, center.y + 1*PIXELS_PER_SQUARE)]
        Shape.__init__(self, coords, "red")

class S_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x - 1*PIXELS_PER_SQUARE, center.y + 1*PIXELS_PER_SQUARE),
                  Point(center.x + 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x, center.y),
                  Point(center.x, center.y + 1*PIXELS_PER_SQUARE)]
        Shape.__init__(self, coords, "green")

class T_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x - 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x + 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x, center.y),
                  Point(center.x, center.y + 1*PIXELS_PER_SQUARE)]
        Shape.__init__(self, coords, "yellow")

class Z_shape(Shape):

    def __init__(self, center):
        coords = [Point(center.x - 1*PIXELS_PER_SQUARE, center.y),
                  Point(center.x + 1*PIXELS_PER_SQUARE, center.y + 1*PIXELS_PER_SQUARE),
                  Point(center.x, center.y),
                  Point(center.x, center.y + 1*PIXELS_PER_SQUARE)]
        Shape.__init__(self, coords, "magenta")
        

'''
win = GraphWin("Tetrominoes", 150, 150)
# the block is drawn at position (1, 1) on the board
block = Block(Point(1, 1), "red")
# the __init__ method for your block should deal with converting
# the Point into pixels
block.draw(win)
win.mainloop()
'''

win = GraphWin("Tetrominoes", 900, 150)
# a list of shape classes
tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
x = 3*PIXELS_PER_SQUARE
for tetromino in tetrominoes:
    shape = tetromino(Point(x, 1*PIXELS_PER_SQUARE))
    shape.draw(win)
    x += 4*PIXELS_PER_SQUARE
win.mainloop()
