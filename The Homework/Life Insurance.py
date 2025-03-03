class Circle:
    def __intit__ (self,radius,height):
        self.radius = radius
        self.height = height

    def display(self):
        print("The area of the circle",(22/7)*self.radius*self.radius)

class Triangle(Circle):
    def __init__ (self,radius,height):
        self.radius = radius
        self.height = height

    def display(self):
        print("The area of a right-angled triangle",(1/2)*self.radius*self.height)

obj = Circle()
obj = Triangle(5,6)
obj.display()