#ex14
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Nhap n: "))
if is_prime(n):
    print("n la so nguyen to")
else:
    print("n khong phai la so nguyen to")