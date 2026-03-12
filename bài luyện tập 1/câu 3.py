
# Yêu cầu người dùng nhập vào một số trong khoảng từ 1 đến 9 và hiển thị bảng cửu chương

while True:
    try:
        # Yêu cầu người dùng nhập số
        num_str = input("Nhập một số từ 1 đến 9: ")
        number = int(num_str)

        # Kiểm tra xem số có nằm trong khoảng hợp lệ không
        if 1 <= number <= 9:
            # In bảng cửu chương
            print(f"Bảng cửu chương của {number}:")
            for i in range(1, 10):
                print(f"{number} x {i} = {number * i}")
            break  # Thoát khỏi vòng lặp nếu đầu vào hợp lệ và đã in bảng
        else:
            print("Số không hợp lệ. Vui lòng nhập một số trong khoảng từ 1 đến 9.")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng chỉ nhập số nguyên.")
