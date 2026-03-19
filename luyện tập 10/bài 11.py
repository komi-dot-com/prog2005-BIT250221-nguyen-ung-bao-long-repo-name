import os
import subprocess

def run_exercise(exercise_number):
    file_name = f"bài {exercise_number}.py"
    if os.path.exists(file_name):
        print(f"--- Chạy {file_name} ---")

        try:
            subprocess.run(["python", file_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Lỗi khi chạy {file_name}: {e}")
        except FileNotFoundError:
            print(f"Không tìm thấy trình thông dịch 'python'. Hãy chắc chắn rằng nó đã được cài đặt và trong PATH.")
        print(f"--- Kết thúc {file_name} ---\n")
    else:
        print(f"Không tìm thấy file: {file_name}\n")

def main_menu():
    while True:
        print("======================================")
        print("Chọn một bài tập để chạy:")
        for i in range(1, 11):
            print(f"  {i}. Chạy bài tập {i}")
        print("  0. Thoát")
        print("======================================")

        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
            if choice == 0:
                print("Đã thoát chương trình.")
                break
            elif 1 <= choice <= 11:
                run_exercise(choice)
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 11.\n")
        except ValueError:
            print("Vui lòng nhập một số.\n")

if __name__ == "__main__":
    main_menu()
