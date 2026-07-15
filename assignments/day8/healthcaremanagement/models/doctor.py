from models.person import Person

class Doctor(Person):
    def __init__(self, id, name, age, specialization):
        super().__init__(id, name, age)   # Reuse Person class attributes
        self.specialization = specialization

    def get_details(self):
        details = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "specialization": self.specialization
        }
        return details
    