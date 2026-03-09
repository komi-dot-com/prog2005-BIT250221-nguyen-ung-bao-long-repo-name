#câu 2
import math

print("Các số lẻ từ 111 đến 17 (thứ tự giảm dần):")
for i in range(111, 16, -2):
    print(i, end=' ')
print("\n")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Các số nguyên tố trong khoảng từ 17 đến 111:")
for num in range(17, 112):
    if is_prime(num):
        print(num, end=' ')
print()
