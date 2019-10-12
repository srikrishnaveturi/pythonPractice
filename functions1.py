def piglatin(word):
    a = word[0]
    if a in "aeiou":
        newWord = word + "ay"
    else:
        newWord = word[1::] + a + "ay"
    return newWord
code = piglatin("ess")
print(code)
