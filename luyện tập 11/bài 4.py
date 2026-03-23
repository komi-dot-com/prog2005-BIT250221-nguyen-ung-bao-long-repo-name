def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 5]
print(f"Danh sách ban đầu: {my_list}")
my_list.append(11)
print(f"Danh sách sau khi thêm phần tử 11: {my_list}")

try:
    k = int(input("Nhập giá trị k để đếm số lần xuất hiện: "))
    count = my_list.count(k)
    print(f"Số lần xuất hiện của {k} trong danh sách là: {count}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

prime_sum = 0
for num in my_list:
    if is_prime(num):
        prime_sum += num
print(f"Tổng các số nguyên tố trong danh sách là: {prime_sum}")
my_list.sort()
print(f"Danh sách sau khi sắp xếp: {my_list}")
my_list.clear()
print(f"Danh sách sau khi xóa: {my_list}")
