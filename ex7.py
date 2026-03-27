#ex7
try:
    a = int(input("Nhập số nguyên dương thứ nhất: "))
    b = int(input("Nhập số nguyên dương thứ hai: "))
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")
    raise SystemExit

a0, b0 = a, b

if a <= 0 or b <= 0:
    print("Vui lòng nhập hai số nguyên dương!")
else:
    while b != 0:
        a, b = b, a % b
    print(f"Ước số chung lớn nhất của {a0} và {b0} là: {a}")