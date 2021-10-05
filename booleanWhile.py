import random
guessBoolean = False
rando = random.randint(0,9)
#print(rando)
#remember that inputs are always strings
while guessBoolean == False:
    newGuess = int(input("please enter an integer between 0 and 9: "))
    if newGuess == rando:
        guessBoolean = True
print(newGuess, "is the right number")

