# # Defining a class (Encapsulation)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Method to display details (Abstraction)
#     def get_details(self):
#         return f"{self.name} is {self.age} years old."

# # Inheritance - Student inherits from Person
# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)  # Calling parent constructor
#         self.grade = grade

#     # Overriding method (Polymorphism)
#     def get_details(self):
#         return f"{self.name} is {self.age} years old and in grade {self.grade}."

# # Creating objects
# student1 = Student("Abdullah", 18, "A")
# print(student1.get_details())  # Output: Abdullah is 18 years old and in grade A.


# =============================================================================
class Person:
    def __init__(self, name, age, occ):
        print(f"Person is created with name:  { name}")
        self.name = name
        self.age = age
        self.occupation = occ

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}")


p1 = Person("John Doe", 25, )


