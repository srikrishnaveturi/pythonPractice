#this is an OOP example
class Square():
    definition = "shape"
    def __init__(self,side):
        self.area = side * side
        self.perimeter = 4 * side
mySquare = Square(6)
print(mySquare.definition)
print(mySquare.perimeter)
