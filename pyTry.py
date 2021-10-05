#print("hello python")
#print("I can python")
#print("this is another string")
#myVar1 = "My first variable"
#print(myVar1)
#myInput1 = float(input("please enter a number : "))
#myInput2 = float(input("please enter another number: "))
#answer = myInput1 + myInput2

#print(myInput1, "+",  myInput2, "=", str(answer) )





fullExam = 100
fullAssessment = 50
fullHomework = 25
examPercentage =0
homeWorkPercentage = 0
assessmentPercentage = 0
def percent_assessment(mark):
    percentage = int((mark/fullAssessment)*100)
    return percentage


def percent_exam(mark):
    percentage = int((mark/fullExam)*100)
    return percentage

def percent_homework(mark):
    percentage = int((mark/fullHomework)*100)
    return percentage

def calculate_percentages():
    assessmentPercentage = percent_assessment(assessmentMark)
    examPercentage = percent_exam(examMark)
    homeWorkPercentage = percent_homework(homeworkMark)

    score = (assessmentPercentage + examPercentage + homeWorkPercentage)/3
    return score

def calculate_grade(percentScore):
    percentScore = int(percentScore)
    if percentScore >= 80:
        grade = "A"
    elif percentScore >= 60:
        grade = "B"
    elif percentScore >= 40:
        grade ="C"
    else:
        grade = "fail"
    return grade

studentName = input("please enter your name: ")
examMark = int(input("please enter your exam mark: "))
homeworkMark = int(input("please enter your homework mark: "))
assessmentMark = int(input("please enter your assessment mark: "))

result = calculate_percentages()
yourGrade = calculate_grade(result)
print("your score is ", result, " percent")
print("your grade is ", yourGrade)






#def make_judgement():
#    if assessmentPercentage >= 50 and examPercentage >= 50 and homeWorkPercentage >= 50:








