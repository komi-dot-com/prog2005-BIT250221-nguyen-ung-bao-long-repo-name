#ex4
n = input("Nhap mot so: ").strip()

if n.startswith('-'):
    n = n[1:]

tong = 0
for ch in n:
    if ch.isdigit():
        tong += int(ch)

print("Tong cac chu so:", tong)