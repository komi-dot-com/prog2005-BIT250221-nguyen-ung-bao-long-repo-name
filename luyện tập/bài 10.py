class SinhVien:
    so_luong = 0

    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
        SinhVien.so_luong += 1

    @classmethod
    def dem_so_luong(cls):
        return cls.so_luong

sv1 = SinhVien("Nguyễn Văn A", 20)
sv2 = SinhVien("Trần Thị B", 21)
sv3 = SinhVien("Lê Văn C", 22)

print(f"Số lượng sinh viên được tạo ra là: {SinhVien.dem_so_luong()}")
