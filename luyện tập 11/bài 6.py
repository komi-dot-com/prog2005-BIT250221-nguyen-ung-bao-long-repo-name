def selection_sort_by_age_desc(items):
    n = len(items)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if items[j][1] > items[max_idx][1]:
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
    return items
user_data = {}
total_age = 0
count = 0

print("Nhập thông tin người dùng (nhập tên trống để kết thúc):")
while True:
    name = input("Nhập tên: ")
    if not name:
        break
    
    try:
        age = int(input(f"Nhập tuổi của {name}: "))
        user_data[name] = age
        total_age += age
        count += 1
    except ValueError:
        print("Tuổi không hợp lệ. Vui lòng nhập một số nguyên.")

if count > 0:
    average_age = total_age / count
    print(f"\nTuổi trung bình của mọi người là: {average_age:.2f}")
    user_items = list(user_data.items())
    sorted_user_items = selection_sort_by_age_desc(user_items)
    print("\nDanh sách người dùng sau khi sắp xếp theo tuổi giảm dần:")
    sorted_dict = dict(sorted_user_items)
    for name, age in sorted_dict.items():
        print(f" - {name}: {age} tuổi")
else:
    print("Không có dữ liệu nào được nhập.")
