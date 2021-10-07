import pdb



#def product(n):
#   total = 1
#   for i in n:
#       total *= i 
#   return total

#print(product([4,4,5]))
pdb.set_trace()

def is_prime(x):
    if x <= 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
            return True
myNum = int(input("enter an integer: "))
myBoolResult = is_prime(myNum)
print(myBoolResult)


