import os

def bai1():
    print("Chạy chương trình bài 1")
    os.system("python \"C:/Users/ln740/PycharmProjects/ktgiuaky/câu 1.py\"")

def bai2():
    print("Chạy chương trình bài 2")
    os.system("python \"C:/Users/ln740/PycharmProjects/ktgiuaky/câu 2.py\"")

def bai3():
    print("Chạy chương trình bài 3")
    os.system("python \"C:/Users/ln740/PycharmProjects/ktgiuaky/câu 3.py\"")

def bai4():
    print("Chạy chương trình bài 4")
    os.system("python \"C:/Users/ln740/PycharmProjects/ktgiuaky/câu 4.py\"")

def main():
    while True:
        print("\\nChọn chương trình để chạy:")
        print("1. Bài 1")
        print("2. Bài 2")
        print("3. Bài 3")
        print("4. Bài 4")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-5): ")

        if choice == '1':
            bai1()
        elif choice == '2':
            bai2()
        elif choice == '3':
            bai3()
        elif choice == '4':
            bai4()
        elif choice == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
