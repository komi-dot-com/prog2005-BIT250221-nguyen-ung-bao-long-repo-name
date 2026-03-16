class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age_str = s.split('-')
        age = int(age_str)
        return cls(name, age)

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person1 = Person("minh", 18)
print(person1)

person_string = "long-18"
person2 = Person.from_string(person_string)
print(person2)
