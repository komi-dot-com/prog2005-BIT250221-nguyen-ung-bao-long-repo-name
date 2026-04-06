#bài 1
r=int(input("bán kính= "))
pi=3.14
chu_vi=2*pi*r
print("chu vi hình tròn là: ", chu_vi)
#bài 2
a=int(input("a= "))
b=int(input("b= "))
tổng = a+b
hiệu= a-b
tích = a/b
print("tổng:", tổng)
print("hiệu:", hiệu)
print("tích:", tích)
#bài 3
class book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
#getter
    def get_name(self):
        retu