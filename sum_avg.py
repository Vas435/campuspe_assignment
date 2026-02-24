
count = int(input("How many numbers? "))

if count <= 0:
    print("No numbers entered.")
else:
    num = float(input("Enter number 1: "))
    total = num
    maximum = num
    minimum = num

    for i in range(2, count + 1):
        num = float(input(f"Enter number {i}: "))
        total += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    average = total / count

    print(f"\nSum: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
