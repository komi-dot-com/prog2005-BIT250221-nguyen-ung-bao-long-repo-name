#ex9
try:
    n = int(input("Nhap vao mot so nguyen duong 5 chu so: "))
except ValueError:
    print("Vui long nhap so nguyen hop le!")
    raise SystemExit

if n < 10000 or n > 99999:
    print("Vui long nhap so nguyen duong co 5 chu so!")
else:
    max_digit = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit > max_digit:
            max_digit = digit
        temp //= 10
    print(f"Chu so lon nhat trong {n} la: {max_digit}")
