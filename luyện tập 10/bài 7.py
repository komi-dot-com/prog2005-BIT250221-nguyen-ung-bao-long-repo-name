correct_password = "python123"
user_input = ""
while user_input != correct_password:
    user_input = input("Vui lòng nhập mật khẩu: ")

    if user_input != correct_password:
        print("Mật khẩu sai. Vui lòng thử lại.")

print("Mật khẩu chính xác. Chào mừng bạn!")
