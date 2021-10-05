datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for x in datalist:
    print(type(x))
num2 = 0
for x  in range(7):
    if x ==3 or x == 6:
        continue
    print(x)

#fibinaci series
num1 = 1
num2 = 1
num3 = num1 + num2
fibs = [num1, num2]
for n in range(2,9):
    nextItem = fibs[n-1] + fibs[n-2]
    fibs.append(nextItem)
print(fibs)

#alternative fibinaci

x, y = 0, 1
while y<50:
    print(y)
    x, y = y, x + y






