# class quadrilateral:
#     length = 20
#     width = 30
#     height = 60
# rectangle = quadrilateral()
# area = rectangle.length*rectangle.width*rectangle.height
# print(area)

#Advanced O.O.P.
class quadrilateral:
    def __init__(self,l,w,h):
        self.length = l
        self.height = h
        self.width = w
    def area(self):
        area_rectangle = self.height*self.width*self.length
        print(area_rectangle)
rectangle1 = quadrilateral(20,30,60)
rectangle2 = quadrilateral(700,230,65)
rectangle1.area()
rectangle2.area()