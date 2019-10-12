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
