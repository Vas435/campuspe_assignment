
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True


n = int(input("Enter a single number to check: "))
print(f"{n} is {'a PRIME' if is_prime(n) else 'NOT a prime'} number.")


start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))
primes = [str(i) for i in range(start, end + 1) if is_prime(i)]
print(f"Prime numbers: {', '.join(primes)}")