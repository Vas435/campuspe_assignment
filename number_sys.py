
import math

def factorial(n): return math.factorial(n) if n >= 0 else "Invalid"
def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
def sum_of_digits(n): return sum(int(d) for d in str(abs(n)))
def reverse_number(n): return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
def is_armstrong(n):
    s = str(abs(n))
    p = len(s)
    return n == sum(int(d)**p for d in s)
def gcd(a, b): return math.gcd(a, b)
def lcm(a, b): return abs(a*b) // gcd(a, b) if a and b else 0
def is_perfect(n):
    if n < 2: return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def math_menu():
    while True:
        print("\n1.Factorial 2.Prime 3.Fibonacci 4.SumDigits 5.RevNum")
        print("6.Armstrong 7.GCD 8.LCM 9.PerfectNum 10.Exit")
        c = input("Choice: ")
        if c == '10': break
        
        # Taking inputs based on function requirements
        if c in ['7', '8']:
            a, b = int(input("Num 1: ")), int(input("Num 2: "))
            if c == '7': print(f"GCD: {gcd(a,b)}")
            if c == '8': print(f"LCM: {lcm(a,b)}")
        else:
            n = int(input("Enter number: "))
            if c == '1': print(f"Factorial: {factorial(n)}")
            elif c == '2': print(f"Prime: {is_prime(n)}")
            elif c == '3': print(f"Fibonacci: {fibonacci(n)}")
            elif c == '4': print(f"Sum of digits: {sum_of_digits(n)}")
            elif c == '5': print(f"Reversed: {reverse_number(n)}")
            elif c == '6': print(f"Armstrong: {is_armstrong(n)}")
            elif c == '9': print(f"Perfect number: {is_perfect(n)}")

math_menu()