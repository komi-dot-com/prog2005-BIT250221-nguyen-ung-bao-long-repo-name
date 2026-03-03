#bài 15
def reverse_with_slicing(s):
  return s[::-1]

def reverse_without_slicing(s):

  reversed_s = ""
  for char in s:
    reversed_s = char + reversed_s
  return reversed_s

input_string = input("Nhập vào một chuỗi: ")

reversed_slice = reverse_with_slicing(input_string)
reversed_no_slice = reverse_without_slicing(input_string)
print(f'Chuỗi đảo ngược (sử dụng slicing): "{reversed_slice}"')
print(f'Chuỗi đảo ngược (không sử dụng slicing): "{reversed_no_slice}"')
