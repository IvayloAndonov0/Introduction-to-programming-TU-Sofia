class Person():
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def introduce(self):
        print(f'{self.name} is {self.nationality}')


class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def introduce(self):
        super().introduce()
        print(f'Studying at {self.university} in {self.year_of_study} year')





class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def introduce(self):
        super().introduce()
        print(f'Lecturer at {self.university} with {self.experience} years of experience')
