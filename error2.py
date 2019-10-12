try:
    for i in ['a','b','c']:
        print(i**2)
except:
    for i in ['a','b','c']:
        print(ord(i))
finally:
    print("always executes at the end")
