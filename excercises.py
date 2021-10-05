#Write a Python function to find the Max of three numbers

def find_biggest_of_three(num1, num2, num3):
    
    if num1 > num2 and num1 > num3:
        return num1

    if num2 > num1 and num2 > num3:
        return num2
    if num3 > num1 and num3 > num2:
        return num3

myNum1 = input("enter 1 : ")
myNum2 = input("enter number 2 : ")
myNum3 = input("enter number 3 : ")
myNum4 = input("enter number 4 : ")
myNum5 = input("enter number 5 : ")
myNum6 = input("enter number 6 : ")

myResult = find_biggest_of_three(myNum1, myNum2, myNum3)
myNextResult = find_biggest_of_three(myNum4, myNum5, myNum6)
if myResult > myNextResult:
    print("the biggest int is : ", myResult)
else:
    print("the biggest int is : ", myNextResult)
    

       
    