#câu 1
import math
a= float(input("nhập số a: "))
b= float(input("nhập số b: "))
c= float(input("nhập số c: "))

max_so =max(a, b, c)
min_so =min(a, b, c)

print("số lớn nhất là", max_so)
print("số nhỏ nhất là", min_so)

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình có một nghiệm: x =", x)
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép: x =", x)
    else:
        print("Phương trình vô nghiệm")