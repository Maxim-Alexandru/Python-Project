from domain.business1 import Departments
from domain.business2 import Patients
from infrastructure.repository2 import PatientRepository
import utils

d = Departments(-1, "", -1)
p = Patients("", "", 0, "")
rep = PatientRepository()


class DepartmentsRepository:
    def __init__(self):
        self.__department = []

    def get_all_departments(self):
        """

        :return: a list containing all the departments from the repository
        """
        return self.__department

    def get_size_department(self):
        """

        :return: the length of the list containing the departments
        """
        return len(self.__department)

    def add_department(self, department):
        """

        :param department: a parameter read by the user
        """
        for el in self.__department:
            if department == el:
                raise ValueError("Department already exists.")
        self.__department.append(department)

    def add_patients_to_department(self, patients, department):
        """

        :param patients: a parameter of type PatientsRepository
        :param department: a parameter of type department read by the user
        """
        i = self.get_index(department)
        if 0 > i > self.get_size_department():
            raise ValueError("The department does not exist")
        p = PatientRepository()
        p.delete_all_patients()
        for el in patients.get_all():
            p.add_patient(el)
        self.__department[i].set_patients(p)

    def get_index(self, other):
        """

        :param other: a parameter of type Department used to get the index from the repository
        :return: the index i, an integer type
        """
        for i in range(self.get_size_department()):
            if self.__department[i] == other:
                return i
        return -1

    def get_department_at_index(self, index):
        """

        :param index: an integer type used to get the department from the repository
        :return: the department at the given index
        """
        if 0 > index > self.get_size_department():
            raise ValueError("Index out of range")
        return self.__department[index]

    def get_patients_from_department(self, department):
        """

        :param department: a parameter of type Department used to get the patients
        :return: a list of patients from the given department
        """
        i = self.get_index(department)
        if 0 > i > self.get_size_department():
            raise ValueError("The department does not exist")
        l = []
        return self.__department[i].get_patients()

    def get_a_certain_patient_from_department_by_PNC(self, department, PNC):
        """

        :param department: a parameter of type Department used to get the list of patients
        :param PNC: an integer type parameter used to identify the patient
        :return: a Patient type parameter from the department
        """
        i = self.get_index(department)
        if 0 > i > self.get_size_department():
            raise ValueError("The department does not exist")
        for el in self.__department[i].get_patients().get_all():
            if el.get_PNC() == PNC:
                return el
        return "The patient does not exist"

    def update_patients_from_department(self, department, patients):
        """

        :param department: a Department type parameter where the update will take place
        :param patients: a PatientRepository type parameter which will replace the old list of patients
        """
        self.add_patients_to_department(patients, department)

    def update_department_by_index(self, department, index):
        """

        :param department: a Department type parameter which will replace the old department
        :param index: an integer type parameter used to find a department from repository
        """
        if 0 > index > self.get_size_department():
            raise ValueError("The department does not exist")
        self.__department[index].set_id(department.get_id())
        self.__department[index].set_name(department.get_name())
        self.__department[index].set_number_of_beds(department.get_number_of_beds())
        self.__department[index].set_patients(department.get_patients())

    def delete_patient_from_department(self, patient, department):
        """

        :param patient: a Patient type parameter used to identify the patient who will be deleted from the list
        :param department: a Department type parameter used to get the list of patients
        """
        j = self.get_index(department)
        if 0 > j > self.get_size_department():
            raise ValueError("The department does not exist")
        if patient in self.__department[j].get_patients().get_all():
            self.__department[j].get_patients().delete_a_patient_by_index(
                self.__department[j].get_patients().get_index(patient))

    def delete_department(self, index):
        """

        :param index: an integer type parameter used to identify the department which will be deleted
        """
        if 0 > index > self.get_size_department():
            raise ValueError("The department does not exist")
        del (self.__department[index])

    def delete_all_departments(self):
        """
        this function will delete all the departments from the repository
        """
        for i in range(self.get_size_department() - 1, -1, -1):
            del (self.__department[i])

    def sort_patients_by_PNC(self, department):
        """

        :param department: a Department type parameter where the sorting will take place
        :return: a boolean value if the condition is satisfied in the locally defined function f
        """
        i = self.get_index(department)
        if 0 > i > self.get_size_department():
            raise ValueError("The department does not exist")

        def f(x, y):
            if x.get_PNC() < y.get_PNC():
                return True
            return False

        l = []
        for el in self.__department[i].get_patients().get_all():
            l.append(el)
        l = utils.my_sort(l, f)
        repo = PatientRepository()
        for el in l:
            repo.add_patient(el)
        self.__department[i].set_patients(repo)

    def sort_departments_by_number_of_patients(self):
        """
        this function sorts the departments by their number of patients
        """
        def f(x, y):
            if x.get_patients().get_size() < y.get_patients().get_size():
                return True
            return False

        l = self.__department
        l = utils.my_sort(l, f)

    def sort_patients_from_department_by_age(self, limit):
        """

        :param limit: an integer type parameter used to filter the patients which have age above this limit
        this function sorts the patients from a department by their age
        """
        def f(x, y):
            number_x = 0
            number_y = 0
            for el in x.get_patients().get_all():
                age = str(el.get_PNC() % 1000000)
                age = age[0:2]
                if not (age[0] == "0" or age[0] == "1"):
                    if 2018 - 1900 + int(age) > limit:
                        number_x += 1
            for el in y.get_patients().get_all():
                age = str(el.get_PNC() % 1000000)
                age = age[0:2]
                if not (age[0] == "0" or age[0] == "1"):
                    if 2018 - 1900 + int(age) > limit:
                        number_y += 1
            if number_x < number_y:
                return True
            return False

        l = self.__department
        l = utils.my_sort(l, f)

    def sort_departments_and_patients_alphabetically(self):
        """
        this function sorts the departments by their number of patients and also sorts the patients alphabetically
        """
        self.sort_departments_by_number_of_patients()

        def f(x, y):
            if x.get_first_name() == y.get_first_name():
                if x.get_last_name() < y.get_last_name():
                    return True
                return False
            else:
                if x.get_first_name() < y.get_first_name():
                    return True
                return False

        for i in range(self.get_size_department()):
            l = self.__department[i].get_patients().get_all()
            l = utils.my_sort(l, f)
            repo = PatientRepository()
            for el in l:
                repo.add_patient(el)
            self.__department[i].set_patients(repo)

    def search_departments_having_patients_with_a_certain_age(self, limit):
        """

        :param limit: an integer type parameter used to filter the patients which have age bellow this limit
        this function search departments containing patients who have age below the parameter limit
        """
        def f(x):
            age = str(x.get_PNC() % 1000000)
            if len(age) != 6:
                for i in range(6 - len(age)):
                    age = "0" + age
            age = age[0:2]
            if not (age[0] == "0" or age[0] == "1"):
                if int(age) > 20:
                    if 2018 - 1900 + int(age) < limit:
                        return True
            else:
                if 2018 - 2000 + int(age) < limit:
                    return True
            return False

        final_result = []
        for el in self.get_all_departments():
            l = el.get_patients().get_all()
            l = utils.my_search(l, f)
            if len(l) != 0:
                for el1 in self.get_all_departments():
                    for el2 in l:
                        if el1.get_name() == el2.get_disease():
                            final_result.append(el1)
        return final_result

    def search_patients_who_have_a_string_in_their_names(self, st, department):
        """

        :param str: a string type parameter which will be searched for in the names of the patients
        :param department: a Department type parameter used to get the list of patients
        :return: a list containing all the patients that have the string str in their names
        """
        def f(x):
            if st in x.get_first_name() or st in x.get_last_name():
                return True
            return False

        l = department.get_patients().get_all()
        l = utils.my_search(l, f)
        return l

    def search_departments_having_patients_with_a_given_name(self, name):
        """

        :param name: a string type parameter used to identify patients having this name
        :return: a list containing the departments having patients with the name the given string
        """
        def f(x):
            if x.get_first_name() == name:
                return True
            return False

        final_result = []
        for el in self.get_all_departments():
            l = el.get_patients().get_all()
            l = utils.my_search(l, f)
            if len(l) != 0:
                for el1 in self.get_all_departments():
                    for el2 in l:
                        if el1.get_name() == el2.get_disease():
                            final_result.append(el1)
        return final_result

    def groups_of_patients_with_same_disease(self, department, k):
        """

        :param department: a Department type parameter used to get the list of patients
        :param k: an integer type parameter used to form the groups having the number its value
        :return: the groups of patients verifying the conditions
        """
        def f(x, y):
            if x.get_disease() == y.get_disease():
                return True
            return False

        index = self.get_index(department)

        def build_result(sol):
            res = []
            for i in range(len(sol)):
                res.append(str(self.__department[index].get_patients().get_patient_by_index(sol[i])))
            return res

        for el in utils.my_backtracking(department.get_patients(), f, k):
            print(str(build_result(el)))

    def groups_of_departments_having_patients_wtih_a_certain_name(self, name, p, k):
        def f(x, y):
            if x.get_name() != name or name != y.get_name():
                return False
            if x.get_patients().get_size() <= p and y.get_patients().get_size <= p:
                return True
            return False

        def build_result(sol):
            res = []
            for i in range(len(sol)):
                res.append(str(self.__department[sol[i]]))
            return res

        for el in utils.my_backtracking(self.get_all_departments(), f, k):
            print(str(build_result(el)))
