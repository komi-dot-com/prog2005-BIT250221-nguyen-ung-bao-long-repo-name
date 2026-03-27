#ex 12
n = int(input("Nhap n: "))

tong = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        tong += i

print("Tong cac so le tu 1 den", n, "la:", tong)