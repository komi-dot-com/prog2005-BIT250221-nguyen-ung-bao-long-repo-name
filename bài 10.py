# bài 10
input_str = input("Nhập một danh sách các số, cách nhau bằng dấu phẩy: ")
numbers_str = input_str.split(',')
numbers = []
for num_str in numbers_str:
    try:
        numbers.append(int(num_str.strip()))
    except ValueError:
        print(f"Bỏ qua giá trị không hợp lệ: {num_str}")

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Các số chẵn trong danh sách là:", even_numbers)

sum_of_evens = sum(even_numbers)
print("Tổng của các số chẵn là:", sum_of_evens)
