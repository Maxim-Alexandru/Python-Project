from domain.business2 import Patients

p = Patients("", "", 0, "")


class PatientRepository:
    def __init__(self):
        self.__l = []

    def get_size(self):
        return len(self.__l)

    def get_all(self):
        return self.__l

    def add_patient(self, patient):
        for el in self.__l:
            if patient == el:
                raise ValueError("Patient already exists")
        self.__l.append(patient)

    def get_index(self, patient):
        if self.get_size() == 1:
            if self.__l[0] == patient:
                return 0
        else:
            for i in range(len(self.__l)):
                if patient == self.__l[i]:
                    return i
        return -1

    def get_patient_by_index(self, index):
        if 0 > index > self.get_size():
            raise ValueError("Index out of range.")
        return self.__l[index]

    def get_patient_by_name(self, first_name, last_name):
        l = []
        for el in self.__l:
            if el.get_first_name() == first_name and el.get_last_name() == last_name:
                l.append(el)
        return l

    def get_patients_with_the_same_disease(self, disease):
        l = []
        for el in self.__l:
            if el.get_disease() == disease:
                l.append(el)
        return l

    def get_patients_with_a_given_letter(self, letter):
        l = []
        for el in self.__l:
            if el.get_first_name()[0] == letter:
                l.append(el)
        return l

    def add_new_disease(self, disease, patient):
        i = self.get_index(patient)
        if 0 > i > self.get_size():
            raise ValueError("Index out of range")
        st = self.__l[i].get_disease() + ", " + disease
        self.__l[i].set_disease(st)

    def update_disease(self, disease, patient):
        i = self.get_index(patient)
        if 0 > i > self.get_size():
            raise ValueError("Index out of range")
        self.__l[i].set_disease(disease)

    def get_index_by_PNC(self, PNC):
        for i in range(len(self.__l)):
            if self.__l[i].get_PNC() == PNC:
                return i
        return -1

    def update_patient_by_PNC(self, patient, PNC):
        i = self.get_index_by_PNC(PNC)
        if 0 > i > self.get_size():
            raise ValueError("Index out of range")
        self.__l[i].set_first_name(patient.get_first_name())
        self.__l[i].set_last_name(patient.get_last_name())
        self.__l[i].set_disease(patient.get_disease())

    def update_patient_by_index(self, patient, index):
        if 0 > index > self.get_size():
            raise ValueError("Index out of range")
        self.__l[index].set_first_name(patient.get_first_name())
        self.__l[index].set_last_name(patient.get_last_name())
        self.__l[index].set_disease(patient.get_disease())

    def delete_a_patient_by_index(self, index):
        if 0 > index > self.get_size():
            raise ValueError("Index out of range")
        del(self.__l[index])

    def delete_patients_with_a_given_disease(self, disease):
        for i in range(self.get_size()-1, -1, -1):
            if self.__l[i].get_disease() == disease:
                del(self.__l[i])

    def delete_patient_by_PNC(self, PNC):
        i = self.get_index_by_PNC(PNC)
        if 0 > i > self.get_size():
            raise ValueError("Index out of range")
        del(self.__l[i])

    def delete_all_patients(self):
        for i in range(self.get_size()-1, -1, -1):
            del(self.__l[i])

    def delete_patients_from_a_given_interval(self, start, stop):
        if 0 > start > self.get_size():
            raise ValueError("Index out of range.")
        if 0 > stop > self.get_size():
            raise ValueError("Index out of range.")
        if start == stop:
            del(self.__l[start])
        if start > stop:
            for i in range(start, stop-1, -1):
                del(self.__l[i])
        else:
            for i in range(stop, start-1, -1):
                del(self.__l[i])







