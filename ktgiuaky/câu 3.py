#câu 3
n = int(input("nhập n: "))

print("Hình 1")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Hình 2")
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    if i == 1:
        print("*")
    elif i == n:
        print("* " * n)
    else:
        print("*", end="")
        print(" " * (2 * i - 3), end="")
        print("*")
