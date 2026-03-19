input_string = input("Nhập vào một chuỗi: ")
if not input_string:
    print("Lỗi: Chuỗi không được để trống.")
else:
    length = len(input_string)
    print(f"Độ dài của chuỗi là: {length}")
