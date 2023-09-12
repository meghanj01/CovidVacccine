from uuid import uuid4
from datetime import datetime, timedelta
import Config
from random import randint
# class Hospital():
#     def __init__(self, hospital_name, slots, pincode):
#         self.hospital_name = hospital_name
#         self.slots = slots
#         self.pincode = pincode

# hospital_list = []
# def add_hospitals():
#     hospital1 = Hospital("XYZ Hospital", 10, "12627")
#     hospital2 = Hospital("ABC Hospital", 11, "12345")
#     hospital3 = Hospital("DEF Hospital", 12, "12347")
#     hospital_list.extend([hospital1, hospital2, hospital3]) 
#     return

class Apponiments():
    hospital_list = ["Hospital A", "Hospital B", "Hospital C"]
    available_appointments = []
    booked_appointments = []
    def __init__(self, date, time, hospital_name):
        self.date = date
        self.time = time
        
        if hospital_name in Apponiments.hospital_list:
            self.hospital_name = hospital_name
        else:
            print("Hospital does not exist")
            return 
        self.available = True
        self.appointment_id =None
        Apponiments.available_appointments.append(self)

    @staticmethod
    def book_slots(date, time, hospital_name):
            for appointment in Apponiments.available_appointments:
                 if (appointment.date).strftime(Config.DATE_FORMAT) == date and appointment.time == time \
                    and (appointment.hospital_name).lower() == hospital_name.lower():
                    Apponiments.available_appointments.remove(appointment)
                    Apponiments.booked_appointments.append(appointment)
                    appointment.appointment_id = randint(0,9999)
                    return f'Your slot is booked for Day: {date}, Time: {time} in {hospital_name} ' \
                        f'and the appointment ID is: {appointment.appointment_id}'
            return 'Slot is already booked'
    
    @staticmethod
    def cancel_solts(appointment_id):
        for appointment in Apponiments.booked_appointments:
            if appointment.appointment_id == appointment_id:
                 appointment.available = True
                 appointment.appointment_id = None
                 return f'Your appointment: {appointment_id} is cancelled successfully'
        return 'Invalid appointment ID or your appointment is already been cancelled'
    
    @staticmethod
    def get_booked_appointments(cls):
        booked_appointments_info = []
        for appointment in cls.booked_appointments:
            booked_appointments_info.append({
                'appointment_id': appointment.appointment_id,
                'date': appointment.date,
                'time': appointment.time,
                'hospital_name': appointment.hospital_name
            })
        return booked_appointments_info
    
    @staticmethod
    def get_available_appointments():
        available_appointments_info = []
        for appointment in Apponiments.available_appointments:
            available_appointments_info.append({
                'date': appointment.date.strftime('%Y-%m-%d'),
                'time': appointment.time,
                'hospital_name': appointment.hospital_name
            })
        return available_appointments_info

    @staticmethod
    def get_reschedule_appointments(appointment_id, date, time, hospital_name):
        cancellation_appointment = None
        for appointment in Apponiments.booked_appointments:
            if appointment.appointment_id == appointment_id:
                 cancellation_appointment = appointment
                 
            # response Apponiments.book_slots(date, time, hospital_name)
        for appointment in Apponiments.available_appointments:
                if (appointment.date).strftime(Config.DATE_FORMAT) == date and appointment.time == time \
                and (appointment.hospital_name).lower() == hospital_name.lower():
                    if cancellation_appointment:
                        cancellation_appointment.available = True
                        cancellation_appointment.appointment_id = None
                        Apponiments.available_appointments.remove(appointment)
                        Apponiments.booked_appointments.append(appointment)
                        appointment.appointment_id = randint(0,9999)
                    else:
                         return f'Appointment is not available {appointment_id}'
                    return f'Your slot is booked for Day: {date}, Time: {time} in {hospital_name} ' \
                        f'and the appointment ID is: {appointment.appointment_id}'
        return 'Slot is already booked'

appointments = []
time_list = ['09:00','09:30','10:00','10:30','11:00','11:30','12:00','15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00']

end_date = datetime(2023, 9, 2)

# temporary add appointment function to add dummy values
def add_appointments(): 
    start_date = datetime(2023, 9, 1)
    while start_date <= end_date:
        for hospital in ["Hospital A", "Hospital B", "Hospital C"]:
            for time in time_list:
                appointment = Apponiments(start_date, time, hospital)
                appointments.append(appointment)
        start_date += timedelta(days=1)
    
def book_slots():
        for hospital in ["Hospital A"]:
            for appointment in appointments:
                appointment = appointment.book_slots(datetime(2023, 9, 1), '9:00', hospital)


if __name__ == '__main__':
    add_appointments()
    print(Apponiments.get_available_appointments())
    book_slots()
    print(Apponiments.get_booked_appointments())


#we can also write patient class and attach appoint _ids with Patient data
# class patient():
#     id
#     insurance_number
#     phone_number
#     patient_name
#     age
#     history
