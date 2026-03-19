def bubble_sort_by_length_desc(arr):
    n = len(arr)
    print(f"Chuỗi ban đầu: {arr}\n")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        print(f"Sau lần lặp thứ {i + 1}: {arr}")

        if not swapped:
            print("\nDanh sách đã được sắp xếp xong.")
            break
    return arr


string_list = []
print("Vui lòng nhập 5 chuỗi bất kỳ.")
for i in range(5):
    while True:
        user_input = input(f"Nhập chuỗi thứ {i + 1}: ")
        if user_input:
            string_list.append(user_input)
            break
        else:
            print("Chuỗi không được để trống. Vui lòng nhập lại.")

sorted_list = bubble_sort_by_length_desc(string_list)
print(f"\nDanh sách chuỗi sau khi sắp xếp (độ dài giảm dần): {sorted_list}")
