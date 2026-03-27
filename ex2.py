#ex2
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        s = input("Nhập một số nguyên dương: ").strip()
        try:
            n = int(s)
            if n <= 0:
                print("Vui lòng nhập số nguyên dương (> 0).")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")

if __name__ == "__main__":
    main()