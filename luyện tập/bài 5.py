class User:
    def __init__(self, user_id):
        self._id = user_id

    @property
    def id(self):
        return self._id


if __name__ == "__main__":
    user_id = input("Nhập ID người dùng: ")
    user = User(user_id)
    print(f"ID người dùng đã tạo: {user.id}")
