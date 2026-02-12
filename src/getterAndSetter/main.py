# class Person:
#     def __init__(self, name, age, income):
#         self.name = name
#         self.age = age
#         self.income = income


#     def greet(self):
#         print(
#             f"Hello, my name is {self.name} and I am {self.age} with the income {self.income}"
#         )
#     @property
#     def TenXIncome(self):
#         print(10 * self.income)

#     @TenXIncome.setter
#     def TenXIncome(self, new_income):
#         print(f"new income is {new_income}")

# person1 = Person("Abdullah", 18, 23000)
# # print(person1.income )
# # person1.income = 10
# print(person1.income)
# person1.TenXIncome
# # person1.TenXIncome










class Person:
    def __init__(self, name, age):
        self._name = name  # Using underscore to indicate it's a private attribute
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name
        else:
            raise ValueError("Name cannot be empty")

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("Age must be positive")

# Example usage
person = Person("Alice", 25)
print(person.name)  # Output: Alice
print(person.age)   # Output: 25

person.name = "Bob"  # Changing name using setter
print(person.name)   # Output: Bob

person.age = 30  # Changing age using setter
print(person.age)  # Output: 30

# person.age = -5  # This will raise an error: Age must be positive
