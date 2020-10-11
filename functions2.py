def alternate_casing(mystring):
    '''format a string with alternating cases'''
    n = len(mystring)
    l = list()
    num = 0
    for letter in mystring:        
        if num % 2 == 0:
            l.append(letter.lower())
        else:
            l.append(letter.upper())
        num+=1
    st = str(l)
    return st


text = 'anthro'
print(text)
print(alternate_casing(text))
