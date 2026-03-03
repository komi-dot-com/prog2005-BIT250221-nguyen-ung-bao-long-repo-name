# bài 11
arr = [5, 2, 8, 1, 9, 4]

if not arr:
    print("Mảng rỗng")
else:
    max_val = arr[0]
    min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    print("Giá trị lớn nhất trong mảng là:", max_val)
    print("Giá trị nhỏ nhất trong mảng là:", min_val)
