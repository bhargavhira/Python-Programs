n = int(input("Enter the number of integers: "))

arr = list(map(int, input("Enter the integers: ").split()))
triplets = []

# Will check every possible combination of three numbers
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                triplet = sorted([arr[i], arr[j], arr[k]])
                if triplet not in triplets:  # Ensuring unique triplets
                    triplets.append(triplet)

# Will display the results
print("Number of distinct triplets:", len(triplets))
for triplet in triplets:
    print(triplet)
