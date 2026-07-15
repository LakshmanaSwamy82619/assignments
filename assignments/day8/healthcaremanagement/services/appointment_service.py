class AppointmentService:
    def __init__(self, datastore):
        self.datastore = datastore

    def add_appointment(self, appointment):
        self.datastore["appointments"][appointment.id] = appointment

    def get_appointment(self, appointment_id):
        appointment = self.datastore["appointments"].get(appointment_id)
        if appointment:
            return appointment.display_info()
        return None

    def delete_appointment(self, appointment_id):
        if appointment_id in self.datastore["appointments"]:
            del self.datastore["appointments"][appointment_id]