#Write a Python function to multiply all the numbers in a list

def mult_list(theList):
    res = 1
    for num in theList:
        
        res *= num
    return res

print(mult_list((2,4,-1,-8)))