#bài 2
def calculate_average_score(scores_dict):
  if not scores_dict:
    return 0
  
  total_score = sum(scores_dict.values())
  number_of_students = len(scores_dict)
  average_score = total_score / number_of_students
  return average_score
student_scores = {
    "long": 85,
    "đúc": 92,
    "ánh": 78,
    "ngọc": 95
}

average = calculate_average_score(student_scores)

print(f"Dictionary điểm số của sinh viên: {student_scores}")
print(f"Điểm trung bình của các sinh viên là: {average}")
