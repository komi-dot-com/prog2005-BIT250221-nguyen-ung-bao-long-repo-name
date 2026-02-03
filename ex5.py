#ex5
text = input("Nhap vao mot chuoi: ")
ch = input("Nhap vao mot ky tu: ")

if len(ch) != 1:
    raise ValueError("Vui long nhap chinh xac 1 ky tu.")

count = 0
for c in text:
    if c == ch:
        count += 1

print(f"Ky tu '{ch}' xuat hien {count} lan.")
