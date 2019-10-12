while True:
    try:
        x = int(input("enter the number to  be squared"))
        print(x**2)
        
    except:
        print("enter a number!")
        continue
    else:
        break
