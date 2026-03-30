#A 5, B 4, C 3, D 2, E 1, F 0;
#score
#Credit unit
#gradepoint 
#CGPA

student_name = input("Enter student's name: ")
student_class = input("Enter student's class: ")

subject1 = input("Enter 1st subject: ")
score1 = float(input(f"Enter score for {subject1}: "))
credit_unit1 = int(input(f"Enter credit unit for {subject1}: "))
grade1 = ""
grade_point1 = 0 


subject2 = input("Enter 2nd subject: ")
score2 = float(input(f"Enter score for {subject2}: "))
credit_unit2 = int(input(f"Enter credit unit for {subject2}:"))
grade2 = ""
grade_point2 = 0

subject3 = input("Enter 3rd subject: ")
score3 = float(input(f"Enter score for {subject3}: "))
credit_unit3 = int(input(f"Enter credit unit for {subject3}: "))
grade3 = ""
grade_point3 = 0

if score1 >= 70 and score1 <=100:
    grade1 = "A"
    grade_point1 = 5 * credit_unit1 #5x3 = 15
elif score1 >=60 and score1 <= 69.9:
    grade1 = "B" 
    grade_point1 = 4 * credit_unit1 #4x3 = 12
elif score1 >=50 and score1 <= 59.9:
    grade1 = "C"
    grade_point1 = 3 * credit_unit1 #3x3 = 9
elif score1 >=45 and score1 <= 49.9:
    grade1 = "D"
    grade_point1 = 2 * credit_unit1 #2x3 = 6
elif score1 >=40 and score1 <= 44.9:
    grade1 = "E"
    grade_point1 = 1 * credit_unit1 #1x3 = 3
elif score1 >=0 and score1 <= 39.9:
    grade1 = "F"
    grade_point1 = 0 * credit_unit1 #0x3 = 0
else:
    print("Invalid score")


if score2 >= 70 and score2 <=100:
    grade2 = "A"
    grade_point2 = 5 * credit_unit2
elif score2 >=60 and score2 <= 69.9:
    grade2 = "B"
    grade_point2 = 4 * credit_unit2
elif score2 >=50 and score2 <= 59.9:
    grade2 = "C"
    grade_point2 = 3 * credit_unit2
elif score2 >=45 and score2 <= 49.9:
    grade2 = "D"
    grade_point2 = 2 * credit_unit2
elif score2 >=40 and score2 <= 44.9:
    grade2 = "E"
    grade_point2 = 1 * credit_unit2
elif score2 >=0 and score2 <= 39.9:
    grade2 = "F"
    grade_point2 = 0 * credit_unit2
else:
    print("Invalid score")


if score3 >= 70 and score3 <=100:
    grade3 = "A"
    grade_point3 = 5 * credit_unit3
elif score3 >=60 and score3 <= 69.9:
    grade3 = "B"
    grade_point3 = 4 * credit_unit3
elif score3 >=50 and score3 <= 59.9:
    grade3 = "C"
    grade_point3 = 3 * credit_unit3
elif score3 >=45 and score3 <= 49.9:
    grade3 = "D"
    grade_point3 = 2 * credit_unit3
elif score3 >=40 and score3 <= 44.9:
    grade3 = "E"
    grade_point3 = 1 * credit_unit3
elif score3 >=0 and score3 <= 39.9:
    grade3 = "F"
    grade_point3 = 0 * credit_unit3
else:
    print("Invalid score")


# 15+12+15 = 42/9

cgpa = (grade_point1 + grade_point2 + grade_point3)/(credit_unit1 + credit_unit2 + credit_unit3)

#This is just for presentations
print("*******************************************")
print("*************** Result (CGPA) *************")
print("")
print(f"Name: {student_name}")
print(f"Class: {student_class}")
print("")
print("*******************************************")
print(f"{subject1} -> Score: {score1} -> Grade: {grade1}")
print(f"{subject2} -> Score: {score2} -> Grade: {grade2}")
print(f"{subject3} -> Score: {score3} -> Grade: {grade3}")
print("")
print(f"CGPA: {cgpa: .2f}")
print("********************************************")
print("********************************************")
print("********************************************")