originalWord = input("please enter a word: ")
myLength = len(originalWord)
run = myLength-1

reverseWord =""

while run >= 0:
    reverseWord = reverseWord + originalWord[run]
    
    run = run -1
print(reverseWord)
if reverseWord == originalWord:
    print("this is a palindrome")
else:
    print("Not a palindrome")





