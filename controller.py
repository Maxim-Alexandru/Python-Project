from infrastructure.repository1 import DepartmentsRepository
from infrastructure.repository2 import PatientRepository
from domain.business1 import Departments
from domain.business2 import Patients

d = Departments(-1, "", -1)
p = Patients("", "", 0, "")
repo1 = PatientRepository()
repo2 = DepartmentsRepository()


class Controller:
    def __init__(self, department, patient):
        self.__department = department
        self.__patient = patient

    def get_all_departments(self):
        return self.__department.get_all_departments()

    def get_size_department(self):
        return self.__department.get_size_department()

    def add_department(self, department):
        self.__department.add_department(department)

    def add_patients_to_department(self, patients, department):
        self.__department.add_patients_to_department(patients, department)

    def get_department_at_index(self, index):
        return self.__department.get_department_at_index(index)

    def get_patients_from_department(self, department):
        return self.__department.get_patients_from_department(department)

    def get_a_certain_patient_from_department_by_PNC(self, department, PNC):
        return self.__department.get_a_certain_patient_from_department_by_PNC(department, PNC)

    def update_patients_from_department(self, department, patients):
        self.__department.update_patients_from_department(department, patients)

    def update_department_by_index(self, department, index):
        self.__department.update_department_by_index(department, index)

    def delete_patient_from_department(self, patient, department):
        self.__department.delete_patient_from_department(patient, department)

    def delete_department(self, department):
        self.__department.delete_department(department)

    def delete_all_departments(self):
        self.__department.delete_all_departments()

    def sort_patients_by_PNC(self, department):
        self.__department.sort_patients_by_PNC(department)

    def sort_departments_by_number_of_patients(self):
        self.__department.sort_departments_by_number_of_patients()

    def sort_patients_from_department_by_age(self, limit):
        self.__department.sort_patients_from_department_by_age(limit)

    def sort_departments_and_patients_alphabetically(self):
        self.__department.sort_departments_and_patients_alphabetically()

    def search_departments_having_patients_with_a_certain_age(self, limit):
        return self.__department.search_departments_having_patients_with_a_certain_age(limit)

    def search_patients_who_have_a_string_in_their_names(self, str, department):
        return self.__department.search_patients_who_have_a_string_in_their_names(str, department)

    def search_departments_having_patients_with_a_given_name(self, name):
        return self.__department.search_departments_having_patients_with_a_given_name(name)

    def groups_of_patients_with_same_disease(self, department, k):
        self.__department.groups_of_patients_with_same_disease(department, k)

    def groups_of_departments_having_patients_wtih_a_certain_name(self, name, p, k):
        self.__department.groups_of_departments_having_patients_wtih_a_certain_name(name, p, k)

    def get_size(self):
        return self.__patient.get_size()

    def get_all(self):
        return self.__patient.get_all()

    def add_patient(self, patient):
        self.__patient.add_patient(patient)

    def get_patient_by_index(self, index):
        return self.__patient.get_patient_by_index(index)

    def get_patient_by_name(self, first_name, last_name):
        return self.__patient.get_patient_by_name(first_name, last_name)

    def get_patients_with_the_same_disease(self, disease):
        return self.__patient.get_patients_with_the_same_disease(disease)

    def get_patients_with_a_given_letter(self, letter):
        return self.__patient.get_patients_with_a_given_letter(letter)

    def add_new_disease(self, disease, patient):
        self.__patient.add_new_disease(disease, patient)

    def update_disease(self, disease, patient):
        self.__patient.update_disease(disease, patient)

    def update_patient_by_PNC(self, patient, PNC):
        self.__patient.update_patient_by_PNC(patient, PNC)

    def update_patient_by_index(self, patient, index):
        self.__patient.update_patient_by_index(patient, index)

    def delete_a_patient(self, patient):
        self.__patient.delete_a_patient(patient)

    def delete_patients_with_a_given_disease(self, disease):
        self.__patient.delete_patients_with_a_given_disease(disease)

    def delete_patient_by_PNC(self, PNC):
        self.__patient.delete_patient_by_PNC(PNC)

    def delete_all_patients(self):
        self.__patient.delete_all_patients()

    def delete_patients_from_a_given_interval(self, start, stop):
        self.__patient.delete_patients_from_a_given_interval(start, stop)
