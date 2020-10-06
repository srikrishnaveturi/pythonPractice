#Function will call itself to get nth fibonacci value until argument passed down equals to 1 or 2

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

# For optimal result please enter values below 30
try: 
    value = int(input("Enter Fibonacci Value:\n"))
    print(f"The {value}th Fibonacci Value is {Fibonacci(value)}")
except:
    print("Please only enter integers")
