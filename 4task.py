# As a part of this task we will write few different codes to carry out different activities.

# Using a while loop to display count down from 20 to 0.
num = 20
i = -1
while num >= 0:
    print(num)
    num -= 1

# Using for loop to print out the even number between 1 and 20
for x in range(1, 21):
    if x % 2 == 0:
        print(x)

# Using this for loop we will print the stars as instructed in the activity
stars = "*"
for star in range(0, 5):
    stars = stars + "*"
    print(stars)

import math
# Ask user to enter two different integers to calculate their GCD
integer1 = int(input("Enter the first number: "))
integer2 = int(input("Enter the second number: "))
print(f"The Greatest Common divisor(GCD) of {integer1} and {integer2} is", math.gcd(integer1, integer2))
