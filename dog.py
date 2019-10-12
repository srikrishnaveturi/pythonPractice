class dog():
    def __init__(self,breed,name,spots):
        self.Breed = breed #attributes of the class are written as "self.<attributeName"
        self.Name = name
        self.Spots = spots
    def barking(self):
        print("woof!")
myDog = dog("huskie","tom",3)
print(myDog.Name)
print("says")
myDog.barking()
