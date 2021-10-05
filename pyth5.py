colNum = int(input("how many columns would you like? "))
rowNum = int(input("how many rows would you like? "))
print(colNum*rowNum)

my2DArray = [[0 for col in range(colNum)] for row in range(rowNum)]
print(my2DArray)

for row in range(rowNum):
    for col in range(colNum):
        my2DArray[row][col] = row*col
print(my2DArray)

