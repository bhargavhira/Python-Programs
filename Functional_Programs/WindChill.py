import math

# Taking inputs from the user
t = float(input("Enter the temperature in Fahrenheit: "))
v = float(input("Enter the wind speed in miles per hour: "))

# Calculating wind chill using the correct formula
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

# Displaying the result
print("The wind chill is:", w)
