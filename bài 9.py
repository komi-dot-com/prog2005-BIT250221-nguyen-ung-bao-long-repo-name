# bài 9
input_str = input("Nhập vào một danh sách các số, cách nhau bằng dấu cách: ")

str_numbers = input_str.split()

numbers = []
for num_str in str_numbers:
    try:
        numbers.append(int(num_str))
    except ValueError:
        print(f"'{num_str}' không phải là một số hợp lệ và sẽ được bỏ qua.")

odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

if odd_numbers:
    print("Các số lẻ trong danh sách là:", odd_numbers)
else:
    print("Không có số lẻ nào trong danh sách.")
