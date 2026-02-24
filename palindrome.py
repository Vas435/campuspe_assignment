text = input("Enter word/number: ")
clean_text = str(text).replace(" ", "").lower()
reversed_text = clean_text[::-1]

print(f"Original: {text}")
print(f"Reversed: {text[::-1]}")
if clean_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")