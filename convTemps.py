#°F = (°C × 9/5) + 32.
#C =(F -32)*(5/9)
myInput = input("please enter the temperature using either 'F' or 'C' at the end to show the scale: ")
theNumber = int(myInput[:-1])
theScale = myInput[-1]
print(theNumber)
print(theScale)
if theScale == "C":
    fahrenheit = (theNumber*(9/5)) + 32
    print(fahrenheit, "F")
if theScale == "F":
    centigrade = (theNumber - 32)*(5/9)
    print(centigrade, "C") 





