#to convert an integer to roman numerals

#M = 1000
#L = 50
#C = 100
#X = 10
#I = 1
#D = 500
class Romanconverter:
    def __init__(self, myNum=0, RNum=""):
        myNum 
        RNum 

    def roman_numeral_generator(self, theNum):
        myNum = theNum
        RNum = ""
        while myNum >= 1000:
            RNum = RNum + "M"
            myNum = myNum-1000
        while myNum >= 500:
            RNum = RNum + "D"
            myNum = myNum - 500
        while myNum >= 100:
            RNum = RNum + "C"
            myNum = myNum-100
        while myNum >= 50:
            RNum = RNum + "L"
            myNum = myNum - 50
        while myNum >= 10:
            RNum = RNum + "X"
            myNum = myNum - 10
        while myNum >= 5:
            RNum = RNum + "V"
            myNum = myNum -5
        while myNum > 0:
            RNum = RNum + "I"
            myNum = myNum - 1
        
        #RNum = RNum("CCCCCCCCC", "XM")
        RNum = RNum.replace("CCCC", "CD")
        RNum = RNum.replace("XXXXXXXXX", "XC")
        RNum = RNum.replace("XXXX", "XL")

        RNum = RNum.replace("IIII", "IV")
        return RNum  
    def another_tool(self, theString):
        return "hello world" 
    
    def arabic_numeral_generator(self, romNum):
        myRomNum = romNum.replace("CD", "CCCC")
        myRomNum = myRomNum.replace("XL", "XXXX")



clare = Romanconverter()
targetInt = int(input("enter an integer: "))
romanResult = clare.roman_numeral_generator(targetInt)
print(romanResult)
print(clare.another_tool("pfft"))






