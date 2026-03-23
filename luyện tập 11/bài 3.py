
input_str = input("Nhập vào một danh sách các số, cách nhau bởi dấu cách: ")
numbers_str = input_str.split()

try:
    numbers = [int(num) for num in numbers_str]
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng chỉ nhập các số nguyên.")
    exit()
even_numbers = []
sum_of_evens = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        sum_of_evens += num
print("Các số chẵn trong danh sách là:", even_numbers)
print("Tổng của các số chẵn là:", sum_of_evens)
