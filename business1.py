from domain.business2 import Patients
from infrastructure.repository2 import PatientRepository

p = Patients("", "", 0, "")
r = PatientRepository()


class Departments:
    def __init__(self, id, name, number_of_beds):
        self.__id = id
        self.__name = name
        self.__number_of_beds = number_of_beds
        self.__patients = PatientRepository()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_number_of_beds(self):
        return self.__number_of_beds

    def get_patients(self):
        return self.__patients

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_number_of_beds(self, number_of_beds):
        self.__number_of_beds = number_of_beds

    def set_patients(self, other):
        for el in other.get_all():
            if el.get_disease() == self.get_name() and not (el in self.__patients.get_all()) :
                self.__patients.add_patient(el)

    def __str__(self):
        s = ""
        if self.get_patients() == []:
            l = self.get_patients()
            if len(l) != 0:
                s += "The department of ID " + str(self.get_id()) + ", which serves people suffering from " + self.get_name() + ", having " + str(
                    self.get_number_of_beds()) + " beds has the following patients: " + "\n"
                for i in range(len(l)):
                    s += "\t" + str(l[i]) + "\n"
            else:
                s += "The department of ID " + str(self.get_id()) + ", which serves people suffering from " + self.get_name() + ", having " + str(
                    self.get_number_of_beds()) + " beds, currently has no patients. " + "\n"
        else:
            l = self.get_patients()
            if l.get_size() != 0:
                s += "The department of ID " + str(self.get_id()) + ", which serves people suffering from " + self.get_name() + ", having " + str(
                    self.get_number_of_beds()) + " beds has the following patients: " + "\n"
                for i in range(l.get_size()):
                    s += "\t" + str(l.get_patient_by_index(i)) + "\n"
            else:
                s += "The department of ID " + str(self.get_id()) + ", which serves people suffering from " + self.get_name() + ", having " + str(
                    self.get_number_of_beds()) + " beds, currently has no patients. " + "\n"
        return s

    def __eq__(self, other):
        if self.get_id() == other.get_id():
            return True
        return False



