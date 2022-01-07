class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = self.get_id()

    def get_id(self):
        self.student_id = f'{self.name[0]}{self.last_name}{self.birth_year}'
        return self.student_id


first_name = input()
surname = input()
year_of_birth = input()

new_student = Student(first_name, surname, year_of_birth)

print(new_student.get_id())