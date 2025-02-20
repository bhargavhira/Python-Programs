def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = input("Enter a 4-digit year: ")

if year.isdigit() and len(year) == 4:
    print(f"Yes! {year} is a leap year." if is_leap_year(int(year)) else f"No! {year} is not a leap year.")
else:
    print("Please enter a valid 4-digit year.")
