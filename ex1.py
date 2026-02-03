#ex1
def main():
    while True:
        try:
            n = int(input("Nhập một số (1-9): "))
            if 1 <= n <= 9:
                break
            print("Vui lòng nhập số trong khoảng 1 đến 9.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    main()