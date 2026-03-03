#bài 14
def count_vowels(s):
  vowels = "aeiou"
  count = 0
  for char in s.lower():
    if char in vowels:
      count += 1
  return count

input_string = input("Nhập vào một chuỗi: ")

vowel_count = count_vowels(input_string)
print(f'Số lượng nguyên âm trong chuỗi "{input_string}" là: {vowel_count}')
