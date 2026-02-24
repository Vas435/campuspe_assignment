
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = 1
    step_str = ""

    for i in range(n, 0, -1):
        result *= i
        if step_str == "":
            step_str = str(i)
        else:
            step_str += " × " + str(i)

    if n == 0: 
        step_str = "1"

    print(f"{n}! = {step_str} = {result}")
