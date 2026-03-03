#bài 7
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

try:
    input_str = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
    my_list = [int(num) for num in input_str.split(',')]
    
    target_num = int(input("Nhập số bạn muốn tìm: "))
    index = linear_search(my_list, target_num)

    if index != -1:
        print(f"Số {target_num} được tìm thấy tại chỉ số: {index}")
    else:
        print(f"Số {target_num} không có trong danh sách.")

except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập các số nguyên.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
