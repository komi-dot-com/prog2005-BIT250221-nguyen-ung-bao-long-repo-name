#bài 2
n = int(input("Nhập n: "))

print("\nHình 1:")
for i in range(n):
    print("* " * n)

print("\nHình 2:")
for i in range(1, n + 1):
    print("* " * i)

print("\nHình 3:")
for i in range(n, 0, -1):
    print("* " * i)

print("\nHình 4:")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print("\nHình 5:")
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "* ")

print("\nHình 6:")
for i in range(n, 0, -1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "* ")

print("\nHình 7:")
for i in range(1, n + 1):
    lead = "  " * (n - i)
    if i == 1 or i == n:
        print(lead + "* " * i)
    else:
        print(lead + "* " + "  " * (i - 2) + "* ")

print("\nHình 8:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nHình 9:")
for i in range(1, n + 1):
    lead = " " * (n - i)
    if i == 1:
        print(lead + "*")
    elif i == n:
        print(lead + "* " * n)
    else:
        inner_spaces = " " * (2 * i - 3)
        print(lead + "*" + inner_spaces + "*")

print("\nHình 10:")
for i in range(n, 0, -1):
    lead = " " * (n - i)
    if i == 1:
        print(lead + "*")
    elif i == n:
        print(lead + "* " * n)
    else:
        inner_spaces = " " * (2 * i - 3)
        print(lead + "*" + inner_spaces + "*")
