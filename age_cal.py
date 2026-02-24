from datetime import datetime

date_str = input("Enter your birth date (DD-MM-YYYY): ")
birth_date = datetime.strptime(date_str, "%d-%m-%Y")
now = datetime.now()

age_years = now.year - birth_date.year - ((now.month, now.day) < (birth_date.month, birth_date.day))
delta = now - birth_date
print(f"\nCurrent age: {age_years} years")
print(f"Age in months (approx): {age_years * 12 + (now.month - birth_date.month)}")
print(f"Age in days: {delta.days}")
print(f"Age in hours: {delta.days * 24}")
print(f"Age in minutes: {delta.days * 24 * 60}")
print(f"Years until age 100: {100 - age_years}")