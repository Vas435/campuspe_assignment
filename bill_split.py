bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_pct = float(input("Tax percentage: "))
tip_pct = float(input("Tip percentage: "))

tax_amt = bill * (tax_pct / 100)
after_tax = bill + tax_amt
tip_amt = after_tax * (tip_pct / 100)
total = after_tax + tip_amt
per_person = total / people

print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal:    ₹{bill:.2f}")
print(f"Tax ({tax_pct}%):   ₹{tax_amt:.2f}")
print(f"After tax:   ₹{after_tax:.2f}")
print(f"Tip ({tip_pct}%):   ₹{tip_amt:.2f}")
print(f"Total:       ₹{total:.2f}")
print(f"Per person:  ₹{per_person:.2f}")