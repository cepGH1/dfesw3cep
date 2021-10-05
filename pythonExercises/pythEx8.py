#Write a Python function that takes a list and 
# returns a new list with unique elements of the first list.

def fix_list(myList):
    processedList = []
    for x in myList:
        if x not in processedList:
            processedList.append(x)
    return processedList

theList = [1,2,3,4,4,5]
betterList = fix_list(theList)
print(betterList)


    
