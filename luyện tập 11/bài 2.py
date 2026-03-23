def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

my_list = []

search_term = input("hãy nhập các chuỗi ký tự cần tìm: ")

result = binary_search(my_list, search_term)

if result != -1:
    print("các ký tự cần tìm:", str(result))
else:
    print("các ký tự cần tìm không có trong danh sách")
