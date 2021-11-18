grade = float(input("Input grade: "))

if grade >= 97:
    print("Your grade is 1.0")
    print("Description: Excellent!")
elif grade < 97 and grade >= 94:
    print("Your grade is 1.25")
    print("Description: Excellent!")
elif grade < 94 and grade >= 91:
    print("Your grade is 1.5")
    print("Description: Very Good!")
elif grade < 91 and grade >= 88:
    print("Your grade is 1.75")
    print("Description: Very Good!")
elif grade < 88 and grade >= 85:
    print("Your grade is 2.0")
    print("Description: Good!")
elif grade < 85 and grade >= 82:
    print("Your grade is 2.25")
    print("Description: Very Good!")
elif grade < 82 and grade >= 79:
    print("Your grade is 2.5")
    print("Description: Satisfactory!")
elif grade < 79 and grade >= 76:
    print("Your grade is 2.75")
    print("Description: Satisfactory!")
elif grade == 75:
    print("Your grade is 3.0")
    print("Description: Passing!")
elif grade < 75 and grade >= 65:
    print("Your grade is 5.0")
    print("Description: Failure")
else:
    print("Student has dropped/withdrawn. ")


