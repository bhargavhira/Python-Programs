num = int(input("Enter a number: "))

if num > 1:
    i = 2
    while i * i <= num:
        while num % i == 0:
            print(i)
            num //= i
        i += 1
    if num > 1:
        print (num)
    else:    
        print("Enter a number greater than 1.")
