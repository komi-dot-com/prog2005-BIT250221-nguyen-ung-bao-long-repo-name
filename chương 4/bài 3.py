#bài 3
student_scores = {
    "long": 85,
    "đức": 92,
    "ánh": 78,
    "ngọc": 95
}

key_to_check = "long"

if key_to_check in student_scores:
    print(f"Key '{key_to_check}' tồn tại trong dictionary.")
else:
    print(f"Key '{key_to_check}' không tồn tại trong dictionary.")

key_to_check_2 = "đức"
if key_to_check_2 in student_scores:
    print(f"Key '{key_to_check_2}' tồn tại trong dictionary.")
else:
    print(f"Key '{key_to_check_2}' không tồn tại trong dictionary.")
