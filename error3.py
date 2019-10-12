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
    
