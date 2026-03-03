#bài 12
def them_ma_tran(A, B):
    ket_qua = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return ket_qua

def nhap_ma_tran(m, n):
    ma_tran = []
    print(f"Nhập ma trận có kích thước {m}x{n}:")
    for i in range(m):
        hang = []
        for j in range(n):
            phan_tu = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
            hang.append(phan_tu)
        ma_tran.append(hang)
    return ma_tran

def in_ma_tran(ma_tran, ten_ma_tran):
    print(f"Ma trận {ten_ma_tran}:")
    for hang in ma_tran:
        print(hang)

if __name__ == "__main__":
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))

    A = nhap_ma_tran(m, n)
    B = nhap_ma_tran(m, n)

    in_ma_tran(A, "A")
    in_ma_tran(B, "B")

    C = them_ma_tran(A, B)
    in_ma_tran(C, "C (A + B)")
