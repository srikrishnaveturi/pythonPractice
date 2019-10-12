
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
