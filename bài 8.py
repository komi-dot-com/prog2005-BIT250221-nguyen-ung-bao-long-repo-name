#bài 8
input_str = input("Nhập vào một danh sách các số, cách nhau bằng dấu cách: ")

str_numbers = input_str.split()

numbers = []
for num_str in str_numbers:
    try:
        numbers.append(int(num_str))
    except ValueError:
        print(f"'{num_str}' không phải là một số hợp lệ và sẽ được bỏ qua.")

found = False
for num in numbers:
    if num > 10:
        print(f"Số đầu tiên lớn hơn 10 là: {num}")
        found = True
        break

if not found:
    print("Không có số nào trong danh sách lớn hơn 10.")
