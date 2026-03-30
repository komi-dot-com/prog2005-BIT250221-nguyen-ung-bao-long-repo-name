#bài 1
import math
try:
    num = float(input("Nhập một số: "))
    if num < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm.")
    else:
        result = math.sqrt(num)
        print(f"Căn bậc hai của {num} là {result}")
except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ.")

#bài 2
chuoi = input("Nhập vào một chuỗi: ")
chieu_dai = len(chuoi)
so_ky_tu_a = chuoi.count('a')

print(f"- Chiều dài của chuỗi là: {chieu_dai}")
print(f"- Số ký tự 'a' xuất hiện trong chuỗi là: {so_ky_tu_a}")
#bài 3
tong = 0
print("Các số chẵn từ 1 đến 20 là:")
for i in range(2, 21, 2):
    print(i, end=" ")
    tong += i
print("\nTổng các số chẵn từ 1 đến 20 là:", tong)
#bài 4
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)
try:
    so = int(input("Nhập một số nguyên dương: "))

    if so < 0:
        print("Lỗi: Không thể tính giai thừa cho số âm!")
    else:
        ket_qua = tinh_giai_thua(so)
        print(f"Giai thừa của {so} ({so}!) là: {ket_qua}")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
#bài 5
class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Tên hoa: {self.name}, Màu sắc: {self.color}"
my_flower = Flower("Hoa Hồng", "Đỏ thắm")
print(my_flower)
#bài 6
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
danh_sach = [64, 34, 25, 12, 22, 11, 90]
print(f"Dãy ban đầu: {danh_sach}")
sap_xep = bubble_sort(danh_sach)
print(f"Dãy sau khi sắp xếp (Bubble Sort): {sap_xep}")