def chuan_hoa_ten(ten: str) -> str:
    cac_tu = ten.split()
    cac_tu_chuan = [tu.capitalize() for tu in cac_tu]
    return " ".join(cac_tu_chuan)

ten_nguoi_dung = input("Nhập tên của bạn: ")
ten_da_chuan_hoa = chuan_hoa_ten(ten_nguoi_dung)
print("Tên đã được chuẩn hóa:", ten_da_chuan_hoa)
