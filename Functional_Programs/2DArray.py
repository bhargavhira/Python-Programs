m, n = map(int, [input("Enter the number of rows = "), input("Enter the number of columns = ")])
dtype_map = {"int": int, "float": float, "bool": lambda x: x.lower() == "true"}
dtype = input("Enter data type (int, float, bool) = ").strip()

if dtype in dtype_map:
    print("Enter values row-wise:")
    array = [list(map(dtype_map[dtype], input().split())) for _ in range(m)]
    for row in array:
        print(" ".join(map(str, row)))
else:
    print("Invalid data type")
