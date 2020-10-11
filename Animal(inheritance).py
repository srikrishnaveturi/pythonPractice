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
    def speak(self):
        print("woof woof")
class cat(animal):
    def __init__(self):
        animal.__init__(self)
        print("and i am a cat")
    def speak(self):
        print("meow meow")

dholu = dog()
billu = cat()
for x in (dholu,billu):
    x.speak()

#polymorphism and inheritence 