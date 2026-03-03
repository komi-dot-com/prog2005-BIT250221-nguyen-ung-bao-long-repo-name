# bài 3
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

print(f"Danh sách màu ban đầu: {colors}")

try:
    colors.remove("Green")
    print("Đã xóa màu 'Green' khỏi danh sách.")
except ValueError:
    print("Màu 'Green' không có trong danh sách để xóa.")

print(f"Danh sách màu sau khi thực hiện thao tác: {colors}")
