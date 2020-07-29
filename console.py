from application.controller import Controller, Departments, Patients, PatientRepository, DepartmentsRepository

rep1 = DepartmentsRepository()
rep4 = PatientRepository()
dep = Departments("", "", 0)
pac = Patients("", "", 0, "")


class UI:
    def __init__(self, controller):
        self.__UI = controller

    @staticmethod
    def department_menu():
        s = ""
        s += "The following options for modifying a department are: \n"
        s += "\t 1. Add a department \n"
        s += "\t 2. Add a list of patients to the department \n"
        s += "\t 3. Get the number of departments \n"
        s += "\t 4. Get all department \n"
        s += "\t 5. Get a department at a certain index \n"
        s += "\t 6. Get the patients from a department \n"
        s += "\t 7. Get a certain patient from a department by his personal numeric code \n"
        s += "\t 8. Update patients from a department \n"
        s += "\t 9. Update a department by index \n"
        s += "\t 10. Delete a patient from a certain department \n"
        s += "\t 11. Delete a department by index \n"
        s += "\t 12. Delete all departments \n"
        s += "\t 13. Sort patients from a department by their personal numeric code \n"
        s += "\t 14. Sort departments by their number of patients \n"
        s += "\t 15. Sort patients from department that have the age greater than a given value \n"
        s += "\t 16. Sort departments by their number of patients and sort patients alphabetically \n"
        s += "\t 17. Identify departments which have patients above a certain age \n"
        s += "\t 18. Identify patients from a department who have in their name a certain string \n"
        s += "\t 19. Identify departments which have patients with a given name \n"
        s += "\t 20. Form groups of patients having the same disease \n"
        s += "\t 21. Form groups of departments having a certain number of patients \n"
        s += "\t 22. Print the menu for the patients \n"
        s += "\t 0. Exit the application"
        print(s)

    @staticmethod
    def patients_menu():
        s = ""
        s += "In order to modify one or more patients, you have the following options: \n"
        s += "\t 1) Add a patient \n"
        s += "\t 2) Get the number of patients \n"
        s += "\t 3) Get all the patients \n"
        s += "\t 4) Get a patient by a given index \n"
        s += "\t 5) Get a patient by his name \n"
        s += "\t 6) Get patients having the same disease \n"
        s += "\t 7) Get patients having the a certain letter in their first name \n"
        s += "\t 8) Add a new disease to a patient \n"
        s += "\t 9) Update the disease of a given patient \n"
        s += "\t 10) Update patient by his personal numeric code \n"
        s += "\t 11) Update a patient by a certain index \n"
        s += "\t 12) Delete a patient by his personal numeric code\n"
        s += "\t 13) Delete patients having a certain disease \n"
        s += "\t 14) Delete patients from a given interval \n"
        s += "\t 0) Return to the main menu \n"
        print(s)

    @staticmethod
    def read_positive_integers(msg):
        x = int(input(msg))
        while x < 0:
            x = int(input(msg))
        return x

    @staticmethod
    def read_department():
        id = input("Give id: ")
        name = input("Give name: ")
        number = int(input("Give number of beds: "))
        return Departments(id, name, number)

    @staticmethod
    def read_pacient():
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        PNC = int(input("Please enter the personal numeric code: "))
        disease = input("Please enter the disease that you are suffering from: ")
        return Patients(first_name, last_name, PNC, disease)

    def PatientsMenu(self):
        while True:
            try:
                UI.patients_menu()
                op = UI.read_positive_integers("Please enter an option: ")
                if op == 0:
                    print("\n")
                    break
                if op == 1:
                    patient = UI.read_pacient()
                    self.__UI.add_patient(patient)
                    print("\n")
                if op == 2:
                    print("The total number of patients is ", self.__UI.get_size())
                if op == 3:
                    patients = self.__UI.get_all()
                    if patients == []:
                        print("Currently there are no patients registered in the system")
                    print("At this moment, there are registered the following patients: ")
                    for el in patients:
                        print(el)
                    print("\n")
                if op == 4:
                    index = UI.read_positive_integers("Please enter the index: ")
                    print("The patient at index ", index, "ïs ", self.__UI.get_patient_by_index(index))
                    print("\n")
                if op == 5:
                    name1 = input("Please enter the first name: ")
                    name2 = input("Please enter the last name: ")
                    patient = self.__UI.get_patient_by_name(name1, name2)
                    if patient == []:
                        print("The patient with the given name does not exist")
                    else:
                        for el in patient:
                            print(el)
                    print("\n")
                if op == 6:
                    disease = input("Please enter a disease: ")
                    patients = self.__UI.get_patients_with_the_same_disease(disease)
                    if patients == []:
                        print("There are no patients having this disease")
                    else:
                        for el in patients:
                            print(el)
                    print("\n")
                if op == 7:
                    letter = input("Please introduce a letter: ")
                    patients = self.__UI.get_patients_with_a_given_letter(letter)
                    if patients == []:
                        print("There are no patients that have their name starting with the given letter")
                    else:
                        for el in patients:
                            print(el)
                    print("\n")
                if op == 8:
                    disease = input("Please enter a new disease: ")
                    PNC = UI.read_positive_integers("Please enter the PNC: ")
                    patient = Patients("", "", 0, "")
                    repo = self.__UI.get_all()
                    for el in repo:
                        if el.get_PNC() == PNC:
                            patient = el
                            break
                    self.__UI.add_new_disease(disease, patient)
                    print("\n")
                if op == 9:
                    disease = input("Please enter a new disease: ")
                    PNC = UI.read_positive_integers("Please enter the PNC: ")
                    patient = Patients("", "", 0, "")
                    repo = self.__UI.get_all()
                    for el in repo:
                        if el.get_PNC() == PNC:
                            patient = el
                            break
                    self.__UI.update_disease(disease, patient)
                    print("\n")
                if op == 10:
                    PNC = UI.read_positive_integers("Please enter a personal numeric code: ")
                    patient = Patients(input("Give me first name: "), input("Give me last name: "), PNC,
                                       input("Please enter the disease: "))
                    self.__UI.update_patient_by_PNC(patient, PNC)
                    print("The patient was successfully updated")
                    print("\n")
                if op == 11:
                    index = UI.read_positive_integers("Please enter an index: ")
                    patient = Patients(input("Please enter the first name: "), input("Please enter the last name: "),
                                       int(input("Please enter the personal numeric code: ")),
                                       input("Please enter a disease: "))
                    self.__UI.update_patient_by_index(patient, index)
                    print("The patient was successfully updated")
                    print("\n")
                if op == 12:
                    PNC = UI.read_positive_integers("Please enter a personal numeric code: ")
                    self.__UI.delete_patient_by_PNC(PNC)
                    print("\n")
                if op == 13:
                    disease = input("Please enter a disease: ")
                    self.__UI.delete_patients_with_a_given_disease(disease)
                    print("The patients were successfully deleted ")
                    print("\n")
                if op == 14:
                    start_index = UI.read_positive_integers("Please enter a starting index: ")
                    stop_index = UI.read_positive_integers("Please enter the index where the deleting will end: ")
                    self.__UI.delete_patients_from_a_given_interval(start_index, stop_index)
                    print("The patients were successfully deleted ")
                    print("\n")
            except Exception as ex:
                print("Some errors occurred: " + str(ex))

    def StartMenu(self):
        while True:
            try:
                UI.department_menu()
                op = UI.read_positive_integers("Give me an options: ")
                if op == 0:
                    break
                if op == 1:
                    department = UI.read_department()
                    self.__UI.add_department(department)
                if op == 2:
                    repo = PatientRepository()
                    repo.delete_all_patients()
                    for el in self.__UI.get_all():
                        repo.add_patient(el)
                    id = int(input("Please enter the id of the department: "))
                    d = DepartmentsRepository()
                    d.delete_all_departments()
                    for el in self.__UI.get_all_departments():
                        d.add_department(el)
                    department = Departments(-1, "", -1)
                    for el in d.get_all_departments():
                        if el.get_id() == id:
                            department.set_name(el.get_name())
                            department.set_id(id)
                            department.set_number_of_beds(el.get_number_of_beds())
                    self.__UI.add_patients_to_department(repo, department)
                if op == 4:
                    l = self.__UI.get_all_departments()
                    for el in l:
                        print(el)
                if op == 3:
                    s = ""
                    s += "The number of departments is " + str(self.__UI.get_size_department())
                    print(s)
                if op == 5:
                    index = UI.read_positive_integers("Please enter an index: ")
                    print(self.__UI.get_department_at_index(index))
                if op == 6:
                    id = UI.read_positive_integers("Please enter the id of the department: ")
                    repo = DepartmentsRepository()
                    department = Departments(1, "", 0)
                    for el in repo.get_all_departments():
                        if el.get_id() == id:
                            department = el
                            break
                    l = self.__UI.get_patients_from_department(department)
                    for el in l.get_all():
                        print(el)
                if op == 7:
                    PNC = UI.read_positive_integers("Give me the personal numeric code: ")
                    id = UI.read_positive_integers("Please enter te id of the department: ")
                    department = Departments(1, "", 0)
                    repo = DepartmentsRepository()
                    for el in repo.get_all_departments():
                        if el.get_id() == id:
                            department = el
                            break
                    print(self.__UI.get_a_certain_patient_from_department_by_PNC(department, PNC))
                if op == 8:
                    UI.PatientsMenu(self)
                    repo = PatientRepository()
                    for el in self.__UI.get_all():
                        repo.add_patient(el)
                    id = input("Please enter the id of the department: ")
                    d = DepartmentsRepository()
                    department = Departments(1, "", 0)
                    for el in d.get_all_departments():
                        if el.get_id() == id:
                            department = el
                            break
                    self.__UI.update_patients_from_department(department, repo)
                if op == 9:
                    UI.patients_menu()
                    index = int(input("Please enter an index: "))
                    repo = PatientRepository()
                    department = UI.read_department()
                    department.set_patients(repo)
                    self.__UI.update_department_by_index(department, index)
                if op == 10:
                    PNC = UI.read_positive_integers("Please enter the personal numeric code: ")
                    patient = Patients("", "", PNC, "")
                    repo1 = self.__UI.get_all()
                    for el in repo1:
                        if el.get_PNC() == PNC:
                            patient = el
                            break
                    id = UI.read_positive_integers("Please enter the id of the department: ")
                    department = Departments(id, "", 0)
                    repo2 = self.__UI.get_all_departments()
                    for el in repo2:
                        if el.get_id() == id:
                            department = el
                            break
                    self.__UI.delete_patient_from_department(patient, department)
                if op == 11:
                    index = UI.read_positive_integers("Enter an index: ")
                    self.__UI.delete_department(index)
                if op == 12:
                    self.__UI.delete_all_departments()
                if op == 13:
                    id = UI.read_positive_integers("Please enter the id of the department: ")
                    department = Departments(id, "", 0)
                    repo2 = self.__UI.get_all_departments()
                    for el in repo2:
                        if el.get_id() == id:
                            department = el
                            break
                    self.__UI.sort_patients_by_PNC(department)
                if op == 14:
                    self.__UI.sort_departments_by_number_of_patients()
                if op == 15:
                    limit = int(input("Set a limit of age: "))
                    self.__UI.sort_patients_from_department_by_age(limit)
                if op == 16:
                    self.__UI.sort_departments_and_patients_alphabetically()
                if op == 17:
                    limit = UI.read_positive_integers("Please set an age limit: ")
                    l = self.__UI.search_departments_having_patients_with_a_certain_age(limit)
                    for el in l:
                        print(el)
                if op == 18:
                    st = input("Please enter a string which will be searched for: ")
                    id = UI.read_positive_integers("Please enter the id of the department: ")
                    department = Departments(id, "", 0)
                    repo2 = self.__UI.get_all_departments()
                    for el in repo2:
                        if el.get_id() == id:
                            department = el
                            break
                    l = self.__UI.search_patients_who_have_a_string_in_their_names(st, department)
                    for el in l:
                        print(el)
                if op == 19:
                    name = input("Please enter a name: ")
                    l = self.__UI.search_departments_having_patients_with_a_given_name(name)
                    for el in l:
                        print(el)
                if op == 20:
                    id = UI.read_positive_integers("Please enter the id of the department where you want to form groups: ")
                    department = Departments(id, "", 0)
                    repo2 = self.__UI.get_all_departments()
                    for el in repo2:
                        if el.get_id() == id:
                            department = el
                            break
                    k = UI.read_positive_integers(
                        "Please set a number which will represent the number of patients in a group: ")
                    self.__UI.groups_of_patients_with_same_disease(department, k)
                if op == 22:
                    UI.PatientsMenu(self)
            except Exception as ex:
                print("Some error occurred: " + str(ex))
