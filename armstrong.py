#Armstrong number
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
    



