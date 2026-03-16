class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("giá sản phẩm phải lớn hơn 0")

    def __str__(self):
        return f"giá sản phẩm: {self._price}"


product = Product(100)

print(product)

product.price = 200
print(product)

product.price = -50
print(product)
