class Product:
    def __init__(self, price):
        self._price = None
        self.price = price
    @property
    def price(self):
        """Getter để lấy giá trị của _price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter để thay đổi giá trị của _price với điều kiện kiểm tra."""
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá sản phẩm phải lớn hơn 0.")

    def __str__(self):
        """Hàm để in thông tin price của product."""
        return f"Sản phẩm có giá: {self.price}"

try:
    my_product = Product(100)
    print(my_product)
    my_product.price = 150
    print(f"Giá mới của sản phẩm: {my_product.price}")

    print("\nCố gắng gán giá trị -50...")
    my_product.price = -50
except ValueError as e:
    print(f"Lỗi: {e}")

try:
    print("\nCố gắng tạo sản phẩm với giá 0...")
    invalid_product = Product(0)
except ValueError as e:
    print(f"Lỗi: {e}")

