num = int(input("Enter a positive number to find its harmonic value: "))

if num > 0:
    harmonic_sum = 0.0  # Initializes sum to store harmonic values

    for i in range(1, num + 1):
        harmonic_sum += 1 / i  # Adds each term to the sum

    print(f"The {num}th harmonic value is: {round(harmonic_sum, 3)}")
else:
    print("Please enter a number greater than 0.")  # Error message for invalid input
