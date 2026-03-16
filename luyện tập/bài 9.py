class SinhVien:
    so_luong = 0  # Thuộc tính của lớp để đếm số đối tượng

    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
        SinhVien.so_luong += 1

    def __eq__(self, other):
        """
        Nạp chồng toán tử == để so sánh hai sinh viên theo điểm.
        """
        if not isinstance(other, SinhVien):
            # Không hỗ trợ so sánh với các kiểu khác
            return NotImplemented
        return self.diem == other.diem

    @classmethod
    def dem_so_luong(cls):
        """
        Class method để trả về số lượng đối tượng đã được tạo.
        """
        return cls.so_luong

# Chạy thử
print(f"Số sinh viên ban đầu: {SinhVien.dem_so_luong()}")

sv1 = SinhVien("An", 8.5)
sv2 = SinhVien("Bình", 9.0)
sv3 = SinhVien("Cường", 8.5)

print(f"So sánh điểm của {sv1.ten} và {sv2.ten}: {sv1 == sv2}")
print(f"So sánh điểm của {sv1.ten} và {sv3.ten}: {sv1 == sv3}")

print(f"Tổng số sinh viên đã được tạo: {SinhVien.dem_so_luong()}")
