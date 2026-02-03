#ex 3
try:
    n = int(input("Nhập số lượng số Fibonacci cần in (n > 0): "))

    if n <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    elif n == 1:
        print("Dãy Fibonacci: 0")
    else:
        a, b = 0, 1
        print(f"{n} số đầu tiên trong dãy Fibonacci là:")

        
        for i in range(n):
            print(a, end=" " if i < n - 1 else "\n")


            a, b = b, a + b

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")