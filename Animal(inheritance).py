class animal():
    def __init__(self):
        print("i am an animal")
    def eat(self):
        print("i love eating")
    def running(self):
        print("i love running")
class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print("and i am a dog")
myDog = dog()
myDog.running()
