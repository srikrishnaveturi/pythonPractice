#this is an OOP example
class circle():
    definition = "shape"
    def __init__(self,radius):
        self.area = 3.14 * radius * radius
        self.perimeter = 2 * 3.14 * radius
myCircle = circle(3)
print(myCircle.definition)
print(myCircle.perimeter)
