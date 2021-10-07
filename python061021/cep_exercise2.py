class LetterExercise:
    def __init__(self):
        self.vowel = ["A", "E", "I", "O", "U"]
        self.dashes =["M", "O", "T"]
        self.myChar = "a"

    def is_it_a_vowel(self, theChar):
        return theChar.upper() in self.vowel
    
    def is_it_dashes(self, theChar):
        return theChar.upper() in self.dashes
    
    def whats_it(self, myTest, myChar):
        if myTest=="v":
            res1 = self.is_it_a_vowel(myChar)
            return res1
        if myTest == "m":
            res2 = self.is_it_dashes(myChar)
            return res2

clare = LetterExercise()
myLetter = input("enter a letter: ")
myGroup = input("v or m: ")
result = clare.is_it_a_vowel(myLetter)
result2 = clare.is_it_dashes(myLetter)
print(result)   
print(result2)
result3 = clare.whats_it(myGroup, myLetter)
print(result3)


    

             


