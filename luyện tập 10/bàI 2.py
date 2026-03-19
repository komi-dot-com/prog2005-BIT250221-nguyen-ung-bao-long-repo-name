input_string = input("Nhập vào một chuỗi: ")
input_char = input("Nhập vào một ký tự để đếm: ")

if len(input_char) == 1:
    count = input_string.count(input_char)

    print(f"Ký tự '{input_char}' xuất hiện {count} lần trong chuỗi.")
else:
    print("Vui lòng chỉ nhập một ký tự.")
