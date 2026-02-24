year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if year % 400 == 0:
        reason = "divisible by 400"
    else:
        reason = "divisible by 4 and not divisible by 100"
    print(f"{year} is a leap year because it is {reason}.")
else:
    print(f"{year} is NOT a leap year.")