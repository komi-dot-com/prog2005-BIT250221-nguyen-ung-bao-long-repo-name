#bài 1
def thong_ke_tuple(numbers):
    if not numbers:
        return 0, None, None
    tong = sum(numbers)
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)

    return tong, lon_nhat, nho_nhat


my_tuple = (10, 25, 5, 40, 15)
tong, max_val, min_val = thong_ke_tuple(my_tuple)

print(f"Tổng: {tong}")
print(f"Giá trị lớn nhất: {max_val}")
print(f"Giá trị nhỏ nhất: {min_val}")