#Write a Python function that accepts a string and 
# calculates the number of upper case letters and lower case letters.
def analyse_sentence(sentence):
    lowChar = 0
    upChar = 0
    for char in sentence:
        if char.islower():
            lowChar += 1
        if char.isupper():
            upChar += 1
    result = [lowChar, upChar]
    return result

myString = input("please enter a sentence : ")
results = analyse_sentence(myString)
print(results[0], " lower case letters")
print(results[1], " upper case letters")


