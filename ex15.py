#ex 15
n = int(input("Nhap so nguyen duong: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)