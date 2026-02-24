print("Choose pattern (1-4): ")
choice = input()
n = int(input("Enter height: "))

if choice == '1':
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))
elif choice == '2':
    for i in range(1, n + 1):
        print(" ".join(str(i) for _ in range(i)))
elif choice == '3':
    for i in range(n, 0, -1):
        print(" ".join(str(x) for x in range(i, 0, -1)))
elif choice == '4':
    for i in range(1, n + 1):
        left = "".join(str(x) for x in range(1, i + 1))
        right = "".join(str(x) for x in range(i - 1, 0, -1))
        print(left + right)