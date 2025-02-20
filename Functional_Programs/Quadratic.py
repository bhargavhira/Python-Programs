import math

# Will take inputs from the user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Will calculate the delta
delta = b * b - 4 * a * c

# Will check if roots are real or not
if delta < 0:
    print("No real roots exist.")
else:
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    
    print("The roots of the quadratic equation are:")
    print("Root 1:", root1)
    print("Root 2:", root2)
