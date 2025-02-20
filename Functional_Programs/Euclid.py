import math

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

distance = math.sqrt(x * x + y * y)

print(f"Euclidean distance from (0,0) to ({x}, {y}) is: {distance}")
