# Circles and squares
# Each can be rendered in vector or raster form

class Renderer():
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing a square of side {side}')

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing pixels for square of side {side}')

class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()    

    square = Square(raster, 5)
    square.draw()
    square.resize(2)
    square.draw()    