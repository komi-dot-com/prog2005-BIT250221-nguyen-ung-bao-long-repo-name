def read_matrix(rows, cols, matrix_name):
    print(f"Nhập ma trận {matrix_name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                value = input(f"Nhập phần tử [{i}][{j}]: ")
                if value.strip():
                    try:
                        row.append(int(value))
                        break
                    except ValueError:
                        print("Lỗi: Vui lòng nhập một số nguyên.")
                else:
                    print("Lỗi: Không được để trống giá trị.")
        matrix.append(row)
    return matrix

def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(" ".join(map(str, row)))

while True:
    try:
        rows = int(input("Nhập số hàng: "))
        cols = int(input("Nhập số cột: "))
        if rows > 0 and cols > 0:
            break
        else:
            print("Số hàng và cột phải là số nguyên dương.")
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên.")

matrix1 = read_matrix(rows, cols, "A")
matrix2 = read_matrix(rows, cols, "B")

result_matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

print_matrix(matrix1, "\nMa trận A:")
print_matrix(matrix2, "\nMa trận B:")
print_matrix(result_matrix, "\nMa trận tổng (A + B):")
