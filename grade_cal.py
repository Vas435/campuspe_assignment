
sub1 = int(input("Enter marks for Subject 1 (out of 100): "))
sub2 = int(input("Enter marks for Subject 2 (out of 100): "))
sub3 = int(input("Enter marks for Subject 3 (out of 100): "))
sub4 = int(input("Enter marks for Subject 4 (out of 100): "))
sub5 = int(input("Enter marks for Subject 5 (out of 100): "))

print("\nMarks Obtained:")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\nTotal Marks (out of 500):", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
