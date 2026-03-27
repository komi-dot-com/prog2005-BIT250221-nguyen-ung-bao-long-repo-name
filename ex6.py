#ex6
def giai_thua(n: int) -> int:
    if n < 0:
        raise ValueError("n phải là số nguyên không âm")
    if n in (0, 1):
        return 1
    return n * giai_thua(n - 1)

n = int(input("Nhập n: "))
print(giai_thua(n))