def insertion_sort_strings():
    strings = []
    print("nhập 5 chuỗi bất kỳ")
    for i in range(5):
        s = input(f"chuỗi {i+1}: ")
        strings.append(s)

    print("\n---bắt đầu sắp xếp---")
    print(f"danh sách ban đầu: {strings}\n")

    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >=0 and len (key) > len(strings[j]):
            strings[j+1] = strings[j]
            j -= 1
        strings[j+1] = key
    print(f"bước {i}: chèn '{key}' -> {strings}")
    print("\n---kết quả---")
    print(strings)
insertion_sort_strings()
