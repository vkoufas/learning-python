# Checks the grading of a student based on their score.
mark = int(input("Give the mark of the student: "))
if mark < 60:
    grade = "F"
elif mark < 70:
    grade = "D"
elif mark < 80:
    grade = "C"
elif mark < 90:
    grade = "B"
elif mark <= 100:
    grade = "A"
else:
    grade = "Error! Mark is maximum 100."
print("The grade of the student is:", grade)