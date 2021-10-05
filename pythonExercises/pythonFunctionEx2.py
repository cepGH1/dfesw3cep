#Sample List : (8, 2, 3, 0, 7)
myList = [8, 5, 3, 0, 7]
print(len(myList))
def sum_list(theList):
    sum = 0
    for num in myList:
        
        sum = sum + num
    return sum

print(sum_list(myList))