#bài 1
def process_tuple(input_tuple):

  total = sum(input_tuple)
  maximum = max(input_tuple)
  minimum = min(input_tuple)
  return total, maximum, minimum


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tong, lon_nhat, nho_nhat = process_tuple(my_tuple)

print(f"Tuple ban đầu: {my_tuple}")
print(f"Tổng các phần tử: {tong}")
print(f"Giá trị lớn nhất: {lon_nhat}")
print(f"Giá trị nhỏ nhất: {nho_nhat}")
