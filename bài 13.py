#bài 13
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Nhập vào một chuỗi: ")
if is_palindrome(input_string):
    print(f'"{input_string}" là một chuỗi palindrome.')
else:
    print(f'"{input_string}" không phải là một chuỗi palindrome.')
