import matplotlib.pyplot as plt
ket_qua = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]
plt.bar(ket_qua, so_luong)

plt.title('Kết quả học tập của lớp')
plt.xlabel('Xếp loại')
plt.ylabel('Số lượng học sinh')
plt.show()
