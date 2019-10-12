class atharva():
    def __init__(self,bodytype):
        self.bodytype= bodytype
        print("my name is atharva")
    def interests(self):
        print("i like slippers")
    def opinions(self):
        print("cats are better than dogs")
class varun(atharva):
    def __init__(self):
        atharva.__init__(self)
        print("hi i am varun")
    def opinions(self):
        print("srikrishna stud hai")
myPerson = varun()
myPerson.opinions()
