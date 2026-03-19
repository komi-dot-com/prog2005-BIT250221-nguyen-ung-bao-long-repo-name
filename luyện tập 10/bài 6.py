input_string = input("Nhập vào một chuỗi để đảo ngược: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(f"Chuỗi đảo ngược là: {reversed_string}")
