import math

# Nhập hai số từ người dùng
try:
    num1 = float(input("Nhập số thứ nhất: "))
    num2 = float(input("Nhập số thứ hai: "))

    # Lũy thừa
    luy_thua = num1 ** num2
    print(f"{num1} lũy thừa {num2} = {luy_thua}")

    # Căn bậc 2 (của số thứ nhất)
    if num1 >= 0:
        can_bac_2 = math.sqrt(num1)
        print(f"Căn bậc hai của {num1} = {can_bac_2}")
    else:
        print(f"Không thể tính căn bậc hai của số âm {num1}")

    # Chia lấy phần nguyên
    if num2 != 0:
        chia_nguyen = num1 // num2
        print(f"{num1} chia lấy phần nguyên cho {num2} = {chia_nguyen}")
    else:
        print("Không thể chia cho 0")

    # Chia lấy phần dư
    if num2 != 0:
        chia_du = num1 % num2
        print(f"{num1} chia lấy phần dư cho {num2} = {chia_du}")
    else:
        print("Không thể chia cho 0")

    # Làm tròn số (làm tròn số thứ nhất)
    print(f"Làm tròn số {num1}:")
    print(f" - Làm tròn xuống: {math.floor(num1)}")
    print(f" - Làm tròn lên: {math.ceil(num1)}")
    print(f" - Làm tròn đến số nguyên gần nhất: {round(num1)}")

except ValueError:
    print("Vui lòng nhập số hợp lệ.")
except ZeroDivisionError:
    print("Lỗi chia cho 0.")
