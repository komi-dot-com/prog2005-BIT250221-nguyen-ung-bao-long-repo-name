#ex10
def tong_1_den_n(n: int) -> int:
    if n <= 0:
        return 0
    return n + tong_1_den_n(n - 1)

n = int(input("Nhap n: "))
print(tong_1_den_n(n))