#ex8
try:
    n = int(input("Nhap vao mot so nguyen duong: "))
except ValueError:
    print("Vui long nhap so nguyen hop le!")
    raise SystemExit

if n <= 0:
    print("Vui long nhap so nguyen duong!")
else:
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    print(f"So sau khi dao nguoc la: {rev}")
