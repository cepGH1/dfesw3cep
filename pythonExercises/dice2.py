#dice2
import dice1

myRange = int(input("enter a reasonable integer : "))
myNum =[]
for x in range(myRange):
    myNum.append(dice1.throw_adie())
    

myTotal = sum(myNum)
print(myTotal)
myExplanation =""
for j in myNum:
    myExplanation += " + "
    myExplanation += str(j)

    
print(myExplanation, " = ", myTotal)


