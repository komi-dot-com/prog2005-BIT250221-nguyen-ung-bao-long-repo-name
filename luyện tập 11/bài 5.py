my_dict = {'a': 1, 'b': 2, 'c': 3, 'tên': 'long', 'quê': 'hb'}

key_to_check = input("Nhập key bạn muốn kiểm tra: ")

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' tồn tại trong dictionary.")
    print(f"Giá trị tương ứng là: {my_dict[key_to_check]}")
else:
    print(f"Key '{key_to_check}' không tồn tại trong dictionary.")
