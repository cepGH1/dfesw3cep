#Write a Python function that takes a number
#  as a parameter and check the number is prime or not.

def prime_checker(num):
    topRange = num-1
    for x in range(2, topRange):
        if num % x == 0:
            print("number is not a prime number")
            break
    print("is prime")

myNum = int(input("please enter an integer : "))
print(myNum)
prime_checker(myNum)

