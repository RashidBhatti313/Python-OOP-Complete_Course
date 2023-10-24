import pickle
from datetime import date

class Appointment:
    def __init__(self, description, year, month, day) -> None:
        self.description = description
        self.year = year
        self.month = month
        self.day = day

    def OccursOn(self, year, month, day):
        return self.year == year and self.month == month and self.day == day
    
    def __str__(self) -> str:
        return f" Appiontment: {self.description} Date: {self.day}-{self.month}-{self.year}"
    
class Onetime(Appointment):
    def __init__(self, description, year, month, day) -> None:
        super().__init__(description, year, month, day)

class Daily(Appointment):
    def __init__(self, description, year, month, day) -> None:
        super().__init__(description, year, month, day)

    def OccursOn(self, year, month, day):
        return True  # Daily appointments occur every day
    
class Monthly(Appointment):
    def __init__(self, description, year, month, day) -> None:
        super().__init__(description, year, month, day)

    def OccursOn(self, year, month, day):
        return self.day == day  # Monthly appointments occur on the same day of the month
    
class AppointmentBook:
    def __init__(self) -> None:
        self.appointments = []

    def addAppointment(self, appointment):
        self.appointments.append(appointment)

    def getAppointmentOnDate(self, year, month, day):
        matching_appointments = [app for app in self.appointments if app.occursOn(year, month, day)]
        return matching_appointments
    
    def SaveAppointmentsToFiles(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.appointments, file)

    def loadAppointmentsFromFile(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.appointments = pickle.load(file)
        except FileNotFoundError:
            print("File not found. NO appointment loaded.")

def main():
    appointment_book = AppointmentBook()
    while True:
        print("\n Options:")
        print("1. Add an appointment")
        print("2. Find appointments to a date")
        print("3. Save appointments to a file")
        print("4. Load appointments from file")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the description: ")
            year, month, day = map(int, input("Enter the date (2023 09 04)").split())
            
            appointment_type = input("Enter the type of appointment (Onetime/Daily/Monthly): ").split()

            if appointment_type == "Onetime":
                appointment = Onetime(description, year, month, day)
            elif appointment_type == "Daily":
                appointment = Daily(description, year, month, day)
            elif appointment_type == "Monthly":
                appointment = Monthly(description, year, month, day)
            else:
                print("Invalid Appointment type. Appointmnet not added.")
                continue

            appointment_book.addAppointment(appointment)
            print("Appointment added Successfully.")

        elif choice == '2':
            year, month, day = map(int, input("Enter the date (2023 08 08): ").split())
            appointments = appointment_book.getAppointmentOnDate(year, month, day)
            if appointments:
                print("Appointments on that date:")
                for app in appointments:
                    print(app)
            else:
                print("No appointments on that date.")

        elif choice == '3':
            filename = input("Enter the filename to save appointmnets: ")
            appointment_book.SaveAppointmentsToFiles(filename)
            print("Appointments saved to", filename)

        elif choice == '4':
            filename = input("Enter the filename to load appointments from: ")
            appointment_book.loadAppointmentsFromFile(filename)
            print("Appointments loaded from", filename)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
