#this is an OOP example
class Circle():
    definition = "shape"
    def __init__(self,radius):
        self.area = 3.14 * radius * radius
        self.perimeter = 2 * 3.14 * radius
myCircle = Circle(3)
print(myCircle.definition)
print(myCircle.perimeter)
