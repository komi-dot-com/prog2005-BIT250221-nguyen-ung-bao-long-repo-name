def factorial_recursive(n):
  if n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)
try:
  num = int(input("Nhập vào một số nguyên không âm để tính giai thừa: "))
  if num < 0:
    print("Giai thừa không được định nghĩa cho số âm.")
  else:
    result = factorial_recursive(num)
    print(f"Giai thừa của {num} là {result}.")
except ValueError:
  print("Vui lòng nhập một số nguyên hợp lệ.")
