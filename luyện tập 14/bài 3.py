n = int(input("Nhập n: "))

print("\nHình 1:")
for i in range(n):
    print(" ".join(["1"] * n))

print("\nHình 2:")
row = " ".join(str(x) for x in range(1, n + 1))
for i in range(n):
    print(row)

print("\nHình 3:")
for i in range(1, n + 1):
    print(" ".join(str(x) for x in range(1, i + 1)))

print("\nHình 4:")
for i in range(n, 0, -1):
    print(" ".join(str(x) for x in range(1, i + 1)))

print("\nHình 5:")
for i in range(1, n + 1):
    if i == 1:
        print("1")
    elif i == n:
        print(" ".join(str(x) for x in range(1, n + 1)))
    else:
        arr = [" "] * i
        arr[0] = "1"
        arr[-1] = str(i)
        print(" ".join(arr))

print("\nHình 6:")
for i in range(n, 0, -1):
    if i == 1:
        print("1")
    elif i == n:
        print(" ".join(str(x) for x in range(1, n + 1)))
    else:
        arr = [" "] * i
        arr[0] = "1"
        arr[-1] = str(i)
        print(" ".join(arr))

print("\nHình 7:")
for i in range(1, n + 1):
    lead = "  " * (n - i)
    print(lead + "   ".join([str(i)] * i))

print("\nHình 8:")
for i in range(1, n + 1):
    lead = "  " * (n - i)
    left = [str(x) for x in range(1, i)]
    right = [str(x) for x in range(i, 0, -1)]
    print(lead + " ".join(left + right))

print("\nHình 9:")
for i in range(1, n + 1):
    lead = "  " * (n - i)
    if i == 1:
        print(lead + "1")
    elif i == n:
        left = [str(x) for x in range(1, i)]
        right = [str(x) for x in range(i, 0, -1)]
        print(lead + " ".join(left + right))
    else:
        length = 2 * i - 1
        arr = [" "] * length
        arr[0] = "1"
        arr[-1] = "1"
        print(lead + " ".join(arr))
