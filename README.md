# Python3 Programming Basics
This is a collection of code snippets for you to learn Python3 basic programming terminology.

# List of Contents:
1) [Inheritance](https://github.com/srikrishnaveturi/pythonPractice/new/master#inheritance)
2) [OOP](https://github.com/srikrishnaveturi/pythonPractice/new/master#oopobject-oriented-programming)
3) [Error Handling](https://github.com/srikrishnaveturi/pythonPractice/new/master#error-handling)
4) [Functions](https://github.com/srikrishnaveturi/pythonPractice/new/master#functions)
5) [Data Structures](https://github.com/srikrishnaveturi/pythonPractice/new/master#data-structures)
6) [Mathematics]()
6) [Miscellaneous](https://github.com/srikrishnaveturi/pythonPractice/new/master#miscellaneous)
7) [Calculator](https://github.com/srikrishnaveturi/pythonPractice/new/master#calculator)

- ## Inheritance:
_Animal Example_
```
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
```

_Animal Example with Polymorphism_
```
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
```
_Person Example_
```
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
```

- ## OOP(Object Oriented Programming):
_Book Example_
```
class book():
    def __init__(self,author,title,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} in {self.pages} pages" 
    def __len__(self):
        return self.pages
myBook = book("author","title",50)
len(myBook)
print(myBook)
```
_Circle Example_
```
class circle():
    definition = "shape"
    def __init__(self,radius):
        self.area = 3.14 * radius * radius
        self.perimeter = 2 * 3.14 * radius
myCircle = circle(3)
print(myCircle.definition)
print(myCircle.perimeter)
```
_Dog Example_
```
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
```

- ##  Error Handling:
_Example1_
```
try:
    f = open("testFile",mode = "r")
    f.write("writing a  line here")
except:
    print("hey you have an error")
finally:
    print("executed!")
```
_Example2_
```
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    for i in ['a','b','c']:
        print(ord(i))
finally:
    print("always executes at the end")
```
_Example3_
```
x = int(input("give the numerator"))
y = int(input("give the denominator"))
try:
    z = x/y
    print(z)
except:
    y = 1
    z = x/y
    print("since you gave the denominat0r as zero,it is taken as 1 by default")
    print(z)
finally:
    print("khatam!")
```
_Example4_
```
while True:
    try:
        x = int(input("enter the number to  be squared"))
        print(x**2)
        
    except:
        print("enter a number!")
        continue
    else:
        break
```

- ## Functions:
_Example1_
```
def piglatin(word):
    a = word[0]
    if a in "aeiou":
        newWord = word + "ay"
    else:
        newWord = word[1::] + a + "ay"
    return newWord
code = piglatin("ess")
print(code)
```
_Example2_
``` 
def myfunc(mystring):
    n = len(mystring)
    l = list()
    num = 0
    for letter in mystring:
        
        if num % 2 ==0:
            l.append(letter.lower())
        else:
            l.append(letter.upper())
        num+=1
    st = str(l)
    return st
myfunc('anthro')
```

- ## Data Structures:
_Queue Using Stack_
```
stack1 = list()
stack2 = list()
flag = True
while(flag == True):
    x = int(input("enter 1 to pop and 2 to push and 3 to exit : "))
    if x == 1:
            stack1 = stack1[:len(stack1)-1]
    elif x == 2:
        y = int(input("enter the number to be entered : "))
        stack2.append(y)
        if len(stack1) == 0:
            stack1.append(stack2[0])
            stack2 = stack2[1:]
    else:
        flag = False
    print("the queue is : ")
    print(stack1[::-1],stack2)
```
- ##  Mathematics:
_Maximum number of points on a line_
```
cor=[]
x=[]
y=[]

cor=input("Enter the coordinate points")
cor=cor.split(" ")
for i in range(len(cor)):
    if i%2==0:
        x.append(int(cor[i]))
    else:
        y.append(int(cor[i]))
        
slope=[]
counts=[]
for i in range(len(x)):
    for j in range(len(x)):
        if i!=j:
            m=(y[j]-y[i])/(x[j]-x[i])
            c=y[i]-(m*x[i])
            slope.append([m,c])
print(slope)
for i in range(len(slope)):
    count=0
    for j in range(len(slope)):
        if (slope[i][0]==slope[j][0]) and (slope[i][1]==slope[j][1] and i!=j):
            count+=1
    counts.append(count)
print((max(counts)+1)/2)
```

_Roman arithmetic_
```
def number(num):
    if(num==1):
        print("I")
    elif(num==5):
        print("V")
    elif(num==10):
        print("X")
    elif(num==50):
        print("L")
    elif(num==100):
        print("C")
    elif(num==500):
        print("D")
    elif(num==1000):
        print("M")
    else:


        while(num>=900):
            if(num>=900 and num<1000):
                print("C",end="")
                num=num+100
            print("M",end="")
            num=num-1000

        while(num>=400):
            if(num>=400 and num<500):
                print("C",end="")
                num=num+100
            print("D",end="")
            num=num-500


        while(num>=90):
            if(num>=90 and num<100):
                print("X",end="")
                num=num+10
            print("C",end="")
            num=num-100

        while(num>=40):
            if(num>=40 and num<50):
                print("X",end="")
                num=num+10
            print("L",end="")
            num=num-50



        while(num>=9):
            if(num==9):
                print("I",end="")
                num=num+1
            print("X",end="")
            num=num-10



        while(num>=4):
            if(num==4):
                print("I",end="")
                num=num+1
            print("V",end="")
            num=num-5


        while(num>=1):
            print("I",end="")
            num=num-1
            
def roman(rom):
    num=0
    for i in range(len((rom))):
        if rom[i]=="I":
            num=num+1
        elif rom[i]=="V":
            if rom[i-1]=="I"and i!=0:
                num=num+3
            else:
                num=num+5
        elif rom[i]=="X":
            if rom[i-1]=="I"and i!=0:
                num=num+8
            else:
                num=num+10
        elif rom[i]=="L":
            if rom[i-1]=="X"and i!=0:
                num=num+30
            else:
                num=num+50
        elif rom[i]=="C":
            if rom[i-1]=="X"and i!=0:
                num=num+80
            else:
                num=num+100
        elif rom[i]=="D":
            if rom[i-1]=="C"and i!=0:
                num=num+300
            else:
                num=num+500
        elif rom[i]=="M":
            if rom[i-1]=="C"and i!=0:
                num=num+800
            else:
                num=num+1000
    return num
    
a=input("Enter first number")
b=input("Enter second number")
c=input("Which operation do you want to perform 1. Add 2.Subtract 3. Multiply 4. Divide")
a=roman(a)
b=roman(b)
if(c=="1"):
    total=a+b
elif(c=="2"):
    total=a-b
elif(c=="3"):
    total=a*b
elif(c=="4"):
    total=a/b
number(total)
```

_Armstrong Number_
```
def Armstrong(n):
    a=str(n)
    m=len(a)
    summation=0
    for i in a:
        summation=summation+int(i)**m

    if(summation==n):
        print("This is an armstrong number")

    else:
        print("not an armstrong number")


number=int(input("Enter number"))
Armstrong(number)
```

_Fibonacci_
```
def Fibonacci(value):
        if value<=0:
            print("Value must not be less than or equal 0")
        # First Fibonacci number is 0
        elif value==1:
            return 0
        # Second Fibonacci number is 1
        elif value==2:
            return 1
        else:
            return Fibonacci(value-1)+Fibonacci(value-2)
            
try: 
    value = int(input("Enter Fibonacci Value:\n"))
    print(f"The {value}th Fibonacci Value is {Fibonacci(value)}")
except:
    print("Please only enter integers")
```

- ## Miscellaneous:
_Sum of an array_
```
ar = [3,4,7,8]
c=0
for n in range(len(ar)):
    c = c + ar[n]
print(c)
```

_Date Time_
```
from datetime import datetime

now = datetime.now()

print("Now it is", now)

print("Now it is", now.strftime('%d %B %Y %H:%M'))
```

- ##  Calculator:
```
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation -\n" \ 
        "1. Add\n" \ 
        "2. Subtract\n" \ 
        "3. Multiply\n" \ 
        "4. Divide\n") 
  
  
# Take input from the user  
select = input("Select operations form 1, 2, 3, 4 :") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == '2': 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == '3': 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == '4': 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input")
```
