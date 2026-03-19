import datetime

class Vehicle:
    MIN_YEAR = 1900

    def __init__(self, make, model, year):
        """Constructor: Khởi tạo một đối tượng Vehicle."""
        self.make = make
        self.model = model
        self.year = year
        print(f"Một chiếc '{self.make} {self.model}' đã được tạo.")


    @property
    def make(self):
        """Getter cho thuộc tính 'make'."""
        return self._make

    @make.setter
    def make(self, value):
        """Setter cho 'make' với xác thực (Cách 1: trực tiếp trong setter)."""
        if not value or not isinstance(value, str):
            raise ValueError("Hãng sản xuất (make) không được để trống và phải là một chuỗi.")
        self._make = value

    @property
    def model(self):
        """Getter cho thuộc tính 'model'."""
        return self._model

    @model.setter
    def model(self, value):
        """Setter cho 'model'."""
        if not value or not isinstance(value, str):
            raise ValueError("Mẫu xe (model) không được để trống và phải là một chuỗi.")
        self._model = value

    @property
    def year(self):
        """Getter cho thuộc tính 'year'."""
        return self._year

    @year.setter
    def year(self, value):
        """Setter cho 'year' với xác thực (Cách 2: gọi hàm validation riêng)."""
        self._validate_year(value)
        self._year = value

    def _validate_year(self, year_value):
        """Hàm riêng để kiểm tra tính hợp lệ của năm sản xuất."""
        if not isinstance(year_value, int) or year_value < self.MIN_YEAR:
            raise ValueError(f"Năm sản xuất phải là số nguyên và không nhỏ hơn {self.MIN_YEAR}.")

    def __str__(self):
        """Trả về biểu diễn chuỗi thân thiện cho người dùng của đối tượng."""
        return f"{self.year} {self.make} {self.model}"

    def __eq__(self, other):
        """So sánh hai đối tượng Vehicle có bằng nhau không."""
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.make == other.make and self.model == other.model and self.year == other.year

    def display_age(self):
        """Tính và hiển thị tuổi của phương tiện."""
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        print(f"Chiếc xe này {age} tuổi.")
        return age

    @classmethod
    def from_string(cls, vehicle_string):
        """Tạo một instance từ một chuỗi có định dạng 'Make-Model-Year'."""
        try:
            make, model, year_str = vehicle_string.split('-')
            year = int(year_str)
            return cls(make, model, year)
        except ValueError:
            print("Chuỗi không đúng định dạng 'Make-Model-Year'.")
            return None

    @staticmethod
    def is_vintage(year):
        """Kiểm tra xem một năm có được coi là 'cổ' (vintage) hay không."""
        return year < 1980


class Car(Vehicle):
    """
    Lớp con kế thừa từ Vehicle, đại diện cho một chiếc ô tô.
    """
    def __init__(self, make, model, year, num_doors):
        """Constructor của lớp Car."""
        super().__init__(make, model, year)
        self.num_doors = num_doors
        print("Đây là một chiếc ô tô.")

    @property
    def num_doors(self):
        """Getter cho num_doors."""
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value):
        """Setter cho num_doors với validation."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Số cửa phải là một số nguyên dương.")
        self._num_doors = value

    def __str__(self):
        """Ghi đè __str__ để thêm thông tin về số cửa."""
        return f"{super().__str__()} - ({self.num_doors} cửa)"

    def display_age(self):
        """Ghi đè display_age để thêm thông tin riêng của Car."""
        print(f"Thông tin tuổi của chiếc ô tô {self.make}:")
        super().display_age()

if __name__ == "__main__":
    print("--- 1. Khởi tạo đối tượng và Constructor ---")
    my_car = Car("Toyota", "Camry", 2021, 4)
    my_motorcycle = Vehicle("Harley-Davidson", "Street 750", 2019)
    print("-" * 20)

    print("\n--- 2. Phương thức __str__ ---")
    print("Xe ô tô:", my_car)
    print("Xe máy:", my_motorcycle)
    print("-" * 20)

    print("\n--- 3. Getter và Setter ---")
    print(f"Hãng sản xuất ban đầu: {my_car.make}")
    my_car.make = "Honda"
    print(f"Hãng sản xuất sau khi đổi: {my_car.make}")
    print("-" * 20)

    print("\n--- 4. Xác thực thuộc tính (ValueError) ---")
    try:
        print("Thử gán năm không hợp lệ...")
        my_car.year = 1890
    except ValueError as e:
        print(f"Lỗi đã bắt được: {e}")
    try:
        print("Thử gán số cửa không hợp lệ...")
        my_car.num_doors = 0
    except ValueError as e:
        print(f"Lỗi đã bắt được: {e}")
    print("-" * 20)

    print("\n--- 5. Phương thức đối tượng (Instance Method) ---")
    my_car.display_age()
    my_motorcycle.display_age()
    print("-" * 20)

    print("\n--- 6. Phương thức lớp (Class Method) ---")
    car_from_string = Car.from_string("Ford-Ranger-2022")
    if car_from_string:
        print(f"Đối tượng tạo từ chuỗi: {car_from_string}")
        print(f"Số cửa của xe mới: {car_from_string.num_doors}") # Thuộc tính của Car
    print("-" * 20)

    print("\n--- 7. Phương thức tĩnh (Static Method) ---")
    print(f"Năm 1975 có phải là vintage không? {Vehicle.is_vintage(1975)}")
    print(f"Năm 2021 có phải là vintage không? {Vehicle.is_vintage(2021)}")
    print("-" * 20)

    print("\n--- 8. Nạp chồng toán tử == ---")
    car1 = Car("VinFast", "VF8", 2023, 4)
    car2 = Car("VinFast", "VF8", 2023, 4)
    car3 = Car("VinFast", "VF9", 2023, 4)
    print(f"car1 == car2? (Cùng thuộc tính): {car1 == car2}")
    print(f"car1 == car3? (Khác model): {car1 == car3}")
    print(f"car1 == my_car? (Khác hoàn toàn): {car1 == my_car}")
    print("-" * 20)
