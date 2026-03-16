def analyze_string(input_string):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0
    space_count = 0
    vowel_count = 0
    consonant_count = 0

    vowels = "aeiouAEIOU"

    for char in input_string:
        if char.isupper():
            upper_count += 1
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.islower():
            lower_count += 1
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            special_count += 1

    print(f"Số lượng chữ cái in hoa: {upper_count}")
    print(f"Số lượng chữ cái in thường: {lower_count}")
    print(f"Số lượng chữ số: {digit_count}")
    print(f"Số lượng ký tự đặc biệt: {special_count}")
    print(f"Số lượng ký tự khoảng trắng: {space_count}")
    print(f"Số lượng nguyên âm: {vowel_count}")
    print(f"Số lượng phụ âm: {consonant_count}")


if __name__ == "__main__":
    user_input = input("Nhập một chuỗi: ")
    analyze_string(user_input)
