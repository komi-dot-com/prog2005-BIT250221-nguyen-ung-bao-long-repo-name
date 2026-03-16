num = input(" nhập 1 số nguyên")

num_clean = num.strip('-')

if not num_clean.isdigit():
    print("hãy nhập số nguyên")
else:
    total =sum(int(d)for d in num_clean)
    print(f"tổng các chữ số của {num} là {total}")
