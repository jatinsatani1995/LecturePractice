class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def rectangle_area(self):
        return self.length*self.width


length1=float(input("Enter Length: "))
width1=float(input("Enter width: "))

newRectangle = Rectangle(length1, width1)


print("Area of Rectangle is: ",newRectangle.rectangle_area())
