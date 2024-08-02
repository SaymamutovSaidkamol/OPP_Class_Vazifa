# Person klassi
class Person:
    def __init__(self, first_name, last_name, profession):
        self._first_name = first_name
        self._last_name = last_name
        self._profession = profession

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def profession(self):
        return self._profession

    def person_info(self):
        return f"{self.first_name} {self.last_name}, kasbi {self.profession}"


class Teacher(Person):
    def __init__(self, first_name, last_name, profession, experience, speciality):
        super().__init__(first_name, last_name, profession)
        self._experience = experience
        self._speciality = speciality

    @property
    def experience(self):
        return self._experience

    @property
    def speciality(self):
        return self._speciality

    def action(self):
        return f"{self.first_name} {self.last_name} - o'z kasbida {self.experience} yil tajribaga ega {self.speciality} mutaxassisi."

    def update_experience(self, new_experience):
        self._experience = new_experience

teacher = Teacher("Falochi", "Pistonchiyev", "O'qituvchi", 10, "Matematika")
print(teacher.person_info()) 
print(teacher.action())  

teacher.update_experience(12)
print(f"Yangi tajriba: {teacher.experience} yil")
