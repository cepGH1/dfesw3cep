#Write a Python function to check whether a number falls in a given range
def check_range(unknown, lower, upper):
    
    if unknown in range(lower, upper):
        print("in range")
    else:
        print("not in range")

check_range(10,2,10)
