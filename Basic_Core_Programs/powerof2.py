num = int(input("Enter power (0-31): "))

if 0 <= num < 31:
    for i in range(1, num):
        print(f"2^{i} = {2**i}")
else:
    print("Number must be between 0 and 31.")