#bài 5
def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

try:
    input_str = input("Nhập danh sách các số thực, cách nhau bằng dấu cách: ")
    float_list = [float(x) for x in input_str.split()]

    insertion_sort_descending(float_list)

    print("Danh sách sau khi sắp xếp giảm dần:")
    print(float_list)

except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng chỉ nhập các số thực.")
