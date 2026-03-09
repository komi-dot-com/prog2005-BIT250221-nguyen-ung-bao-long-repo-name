def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Mảng sau mỗi lần sắp xếp:", arr)

try:
    n = int(input("Nhập số phần tử của mảng: "))
    if n <= 0:
        print("Vui lòng nhập một số nguyên dương cho cỡ của mảng.")
    else:
        my_array = []
        for i in range(n):
            while True:
                try:
                    element = float(input(f"Nhập phần tử thứ {i + 1}: "))
                    my_array.append(element)
                    break
                except ValueError:
                    print("Vui lòng nhập một số hợp lệ.")

        print("Mảng ban đầu:", my_array)
        bubble_sort_descending(my_array)
        print("Mảng sau khi sắp xếp giảm dần:", my_array)

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ cho số phần tử của mảng.")
