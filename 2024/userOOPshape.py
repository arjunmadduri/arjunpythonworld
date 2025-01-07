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
choice = int(input("Please choose ashape to find the volume or area of::: 1. circle, 2. square, 3. rectangle, 4. cube,"))
if choice == 1:
    radius = float(input("Please enter the radius of the circle you want::: "))
    circle = shape(0,0,0,radius)
    circle.circle_area()
if choice == 2:
    length = float(input("Please enter the length of the square you want::: "))
    square = shape(length,0,0,0)
    square.area_square()
if choice == 3:
    length1 = float(input("Please enter the length of the rectangle you want::: "))
    width = float(input("Please enter the width of the rectangle you want::: "))
    rectangle = shape(length1,width,0,0)
    rectangle.area_rectangle
if choice == 4:
    length2 = float(input("please enter the length of the cube you want::: "))
    cube = shape(length2,0,0,0)
    cube.volume_cube()
else:
    print("ERROR. PLEASE TRY AGAIN")
