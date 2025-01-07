# Create a class shape and create the function 
# Area of  circle 
# Area of rectangle 
# ARE of square 
# Volume of cube
class shape:
    def __init__(self,l,w,h,r):
        self.length = l
        self.height = h
        self.width = w
        self.radius = r
    def circle_area(self):
        circles_area = self.radius*self.radius*3.14
        print(circles_area)
    def area_rectangle(self):
        rectangle_area = self.length*self.width
        print(rectangle_area)
    def area_square(self):
        square_area = self.length*self.length
        print(square_area)
    def volume_cube(self):
        cube_volume = self.length*self.length*self.length
        print(cube_volume)
circle = shape(0,0,0,360)
rectangle = shape(30,75,0,0)
square = shape(75,0,0,0)
cube = shape(50,0,0,0)
circle.circle_area()
rectangle.area_rectangle()
square.area_square()
cube.volume_cube()