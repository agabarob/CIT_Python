#A simple grading System for a student's mark.
print("A simple grade system")
input("Enter the student's name:")
input("Enter the subject:")
mark= int(input("Enter the mark:"))
if mark >=80 and mark<100:
    print("Grade : D1")
elif mark >=75 and mark<=79:
    print("Grade : D2")
elif mark >=66 and mark<=79:
    print("Grade : C3")
elif mark >=60 and mark<=65:
    print("Grade : C4")
elif mark >=55 and mark<=59:
    print("Grade : C5")
elif mark >=50 and mark<=54:
    print("Grade : C6")
elif mark >=45 and mark<=49:
    print("Grade : P7")
elif mark >=35 and mark<=44:
    print("Grade : P8")
elif mark >=0 and mark<=34:
    print("Grade : F9")
else:
    print("Invalid mark. Out of range.")