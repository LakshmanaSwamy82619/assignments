class Appointment:
    def __init__(self, id, patient, doctor):
        self.id = id
        self.patient = patient
        self.doctor = doctor

    def display_info(self):
        return (f"Appointment ID: {self.id}, "f"Patient: {self.patient.name}, "f"Doctor: {self.doctor.name}")
    