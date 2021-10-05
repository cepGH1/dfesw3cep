numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
evens=[]
odds = []
for num in numbers:
    if num%2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print("The number of even numbers is ", len(evens))
print("The number of odd numbers is ", len(odds))