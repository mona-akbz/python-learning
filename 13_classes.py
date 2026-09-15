class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My grade is {self.grade}.")


student1 = Student("Mona", 24, 18)

student1.introduce()