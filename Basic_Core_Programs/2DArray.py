m, n = map(int, input().split())
dtype = input().strip()
dtype_map = {"int": int, "float": float, "bool": lambda x: x.lower() == "true"}

if dtype in dtype_map:
    array = []
    for _ in range(m):
        array.append(list(map(dtype_map[dtype], input().split())))
    for row in array:
        print(" ".join(map(str, row)))
else:
    print("Invalid data type")
