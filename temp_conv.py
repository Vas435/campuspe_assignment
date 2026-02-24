
while True:
    print("""
    1. C to F   2. F to C
    3. C to K   4. K to C
    5. F to K   6. K to F
    7. Exit
    """)
    
    choice = input("Choose an option (1-7): ")
    if choice == '7':
        break
    
    temp = float(input("Enter temperature: "))
    
    if choice == '1':
        print(f"Result: {(temp * 9/5) + 32:.2f}°F")
    elif choice == '2':
        print(f"Result: {(temp - 32) * 5/9:.2f}°C")
    elif choice == '3':
        print(f"Result: {temp + 273.15:.2f}K")
    elif choice == '4':
        print(f"Result: {temp - 273.15:.2f}°C")
    elif choice == '5':
        print(f"Result: {(temp - 32) * 5/9 + 273.15:.2f}K")
    elif choice == '6':
        print(f"Result: {(temp - 273.15) * 9/5 + 32:.2f}°F")
    else:
        print("Invalid choice.")
