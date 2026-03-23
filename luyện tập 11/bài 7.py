import csv

def get_employee_info():
    name = input("Nhập tên nhân viên: ")
    age = input("Nhập tuổi nhân viên: ")
    emp_id = input("Nhập ID nhân viên: ")
    return name, age, emp_id

def save_to_txt(name, age, emp_id):
    with open("nhan_vien.txt", "w") as f:
        f.write(f"Tên: {name}\n")
        f.write(f"Tuổi: {age}\n")
        f.write(f"ID: {emp_id}\n")

def save_to_csv(name, age, emp_id):
    with open("nhan_vien.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tên", "Tuổi", "ID"])
        writer.writerow([name, age, emp_id])

def read_and_print_file(filename):
    print(f"\nNội dung file {filename}:")
    with open(filename, "r") as f:
        print(f.read())

if __name__ == "__main__":
    employee_name, employee_age, employee_id = get_employee_info()
    save_to_txt(employee_name, employee_age, employee_id)
    save_to_csv(employee_name, employee_age, employee_id)
    read_and_print_file("nhan_vien.txt")
    read_and_print_file("nhan_vien.csv")
