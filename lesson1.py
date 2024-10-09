# 1. Создать класс Person с атрибутами fullname, age, is_married
class Person:
    def init(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    # 2. Метод introduce_myself, который распечатывает информацию о человеке
    def introduce_myself(self):
        married_status = "Married" if self.is_married else "Not Married"
        print(f"Name: {self.fullname}, Age: {self.age}, Married: {married_status}")


# 3. Класс Student наследует Person и имеет атрибут marks
class Student(Person):
    def init(self, fullname, age, is_married, marks):
        super().init(fullname, age, is_married)
        self.marks = marks

    # 4. Метод для подсчета средней оценки
    def calculate_average(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks)
        return 0

    # Переопределим метод introduce_myself, чтобы также выводить оценки
    def introduce_myself(self):
        super().introduce_myself()
        print(f"Marks: {self.marks}")
        print(f"Average Mark: {self.calculate_average():.2f}")


# 5. Класс Teacher наследует Person и имеет атрибут experience
class Teacher(Person):
    # 6. Атрибут класса base_salary
    base_salary = 30000  # например, базовая зарплата 30,000

    def init(self, fullname, age, is_married, experience):
        super().init(fullname, age, is_married)
        self.experience = experience

    # 7. Метод для расчета зарплаты
    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)  # Бонус начисляется за опыт свыше 3 лет
        bonus = Teacher.base_salary * 0.05 * bonus_years
        return Teacher.base_salary + bonus

    # Переопределим метод introduce_myself, чтобы также выводить информацию о зарплате
    def introduce_myself(self):
        super().introduce_myself()
        print(f"Experience: {self.experience} years")
        print(f"Salary: {self.calculate_salary():.2f}")


# 8. Создать объект учителя и распечатать информацию о нем и его зарплату
teacher = Teacher("John Smith", 45, True, 10)
teacher.introduce_myself()


# 9. Функция create_students, которая создает 3 объекта студента
def create_students():
    student1 = Student("Alice Brown", 16, False, {"Math": 85, "English": 78, "Physics": 92})
    student2 = Student("Bob Johnson", 17, False, {"Math": 88, "English": 82, "History": 90})
    student3 = Student("Charlie Davis", 16, False, {"Math": 75, "English": 70, "Biology": 80})

    return [student1, student2, student3]


# 10. Вызвать функцию create_students и вывести информацию о студентах
students = create_students()
for student in students:
    student.introduce_myself()
    print("-" * 40)  # Разделитель между студентами