age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
tickets = int(input("Number of tickets: "))

if age < 3: base_price = 0
elif age <= 12: base_price = 150
elif age <= 59: base_price = 300
else: base_price = 200

total_base = base_price * tickets

discount_pct = 0.20 if day in ['friday', 'saturday', 'sunday'] else 0
discount_amt = total_base * discount_pct
final_price = total_base - discount_amt

print(f"\nBase price (per ticket): ₹{base_price}")
print(f"Total base amount: ₹{total_base}")
print(f"Discount applied: ₹{discount_amt} ({(discount_pct*100):.0f}%)")
print(f"Final Amount to Pay: ₹{final_price}")