weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

bmi = weight / (height * height)

print(f"\nChỉ số BMI của bạn: {bmi:.2f}")

if bmi < 18.5:
    print("Phân loại: Thiếu cân")
elif bmi < 25:
    print("Phân loại: Bình thường")
elif bmi < 30:
    print("Phân loại: Thừa cân")
else:
    print("Phân loại: Béo phì")