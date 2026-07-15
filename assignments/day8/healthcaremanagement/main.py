from data.datastore import datastore
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from services.healthcare_system import HealthcareSystem

system = HealthcareSystem(datastore)

p1 = Patient(1,"Swamy",30,"Fever")
p2 = Patient(2,"Rahuk",25,"Cold")

d1 = Doctor(101,"Dr.Ravi",45,"General Physician")
d2 = Doctor(102,"Dr.Priya",38,"Cardiologist")

system.patient_service.add_patient(p1)
system.patient_service.add_patient(p2)

system.doctor_service.add_doctor(d1)
system.doctor_service.add_doctor(d2)

a1 = Appointment(1001,p1,d1)
a2 = Appointment(1002,p2,d2)

system.appointment_service.add_appointment(a1)
system.appointment_service.add_appointment(a2)

print(system.patient_service.get_patient(1))
print(system.patient_service.get_patient(2))

print(system.doctor_service.get_doctor(101))
print(system.doctor_service.get_doctor(102))

print(system.appointment_service.get_appointment(1001))
print(system.appointment_service.get_appointment(1002))