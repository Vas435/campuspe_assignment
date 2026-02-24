def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Div by zero"
def modulus(a, b): return a % b if b != 0 else "Error: Div by zero"
def power(a, b): return a ** b

def calculator():
    ops = {'1': add, '2': subtract, '3': multiply, '4': divide, '5': modulus, '6': power}
    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 6.Pow 7.Exit")
        c = input("Choice: ")
        if c == '7': break
        if c in ops:
            a = float(input("First num: "))
            b = float(input("Second num: "))
            print(f"Result: {ops[c](a, b)}")

calculator()