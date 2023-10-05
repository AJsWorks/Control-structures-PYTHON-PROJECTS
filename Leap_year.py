# This is a simple program that can figure out which years are leap years and which are not.

'''
The leap year rule is:
1. If the year is divisible by 4 - it's a leap year.
2. But, if the year is divisible by 100 - it's not a leap year.
3. However, if the year is divisible by 400 - it's a leap year.
'''

# Ask a user to enter a start year and the number of years they want to check
print("Please enter the following information to enquire about leap years.")
start_year = int(input("What year do you want to start with?: "))
years = int(input("How many years do you want to check?: "))
for x in range(start_year, start_year + years):
    # Checking whether it's a leap year or not using if statement.
    if x % 4 == 0 and (x % 100 != 0 or x % 400 ==0):
        print(x, "is a leap year.")
    else:
        print(x, "isn't a leap year.")