import unittest
from infrastructure.repository1 import DepartmentsRepository
from domain.business1 import Departments
from domain.business2 import Patients
from infrastructure.repository2 import PatientRepository

r = DepartmentsRepository()


class DepartmentRepositoryTest(unittest.TestCase):
    def test_add_department(self):
        repo1 = DepartmentsRepository()
        repo2 = PatientRepository()
        patient1 = Patients("G", "K", 111, "flu")
        patient2 = Patients("R", "R", 112, "coma")
        department1 = Departments(1, "flue", 4)
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        department1.set_patients(repo2)
        repo1.add_department(department1)
        department2 = Departments(1, "flu", 5)
        try:
            repo1.add_department(department2)
            assert False
        except Exception as ex:
            assert True
        self.assertEqual(repo1.get_size_department(), 1)

    def test_get_size(self):
        repo1 = DepartmentsRepository()
        repo2 = PatientRepository()
        patient1 = Patients("G", "K", 111, "flu")
        patient2 = Patients("R", "R", 112, "coma")
        department1 = Departments(1, "flue", 4)
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        department1.set_patients(repo2)
        repo1.add_department(department1)
        self.assertEqual(repo1.get_size_department(), 1)

    def test_add_patients_to_department(self):
        repo1 = PatientRepository()
        patient1 = Patients("G", "K", 111, "flu")
        patient2 = Patients("R", "R", 112, "coma")
        patient3 = Patients("A", "B", 1344, "flu")
        repo1.add_patient(patient1)
        repo1.add_patient(patient2)
        repo1.add_patient(patient3)
        department = Departments(1, "flu", 4)
        repo2 = DepartmentsRepository()
        repo2.add_department(department)
        repo2.add_patients_to_department(repo1, department)
        self.assertEqual(department.get_patients().get_size(), 2)

    def test_get_index(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 2)
        department3 = Departments(3, "coma", 5)
        department4 = Departments(4, "flu", 3)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        self.assertEqual(repo1.get_index(department2), 1)
        self.assertEqual(repo1.get_index(department4), -1)

    def test_get_department_by_index(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 2)
        department3 = Departments(3, "coma", 5)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        self.assertEqual(repo1.get_department_at_index(0), department1)

    def test_get_patients_from_department(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo1.add_patients_to_department(repo2, department1)
        self.assertEqual(repo1.get_patients_from_department(department1).get_size(), 3)

    def test_get_a_certain_patient_from_department(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flue", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        patient4 = Patients("L", "K", 0, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo1.add_patients_to_department(repo2, department1)
        self.assertEqual(repo1.get_a_certain_patient_from_department_by_PNC(department1, patient4),
                         "The patient does not exist")
        try:
            self.assertEqual(repo1.get_a_certain_patient_from_department_by_PNC(department1, patient1), patient4)
            assert False
        except Exception as ex:
            assert True

    def test_update_patients_from_department(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flue", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        patient4 = Patients("L", "K", 0, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.delete_all_patients()
        repo2.add_patient(patient4)
        repo1.update_patients_from_department(department1, repo2)
        self.assertEqual(department1.get_patients().get_size(), 0)

    def test_update_department_by_index(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        department2 = Departments(2, "Zika", 3)
        patient4 = Patients("L", "M", 908, "Zika")
        repo2.add_patient(patient4)
        repo1.update_department_by_index(department2, 0)
        self.assertEqual(department1, department2)

    def test_delete_patient_from_department(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo1.add_patients_to_department(repo2, department1)
        repo1.delete_patient_from_department(patient1, department1)
        self.assertEqual(department1.get_patients().get_size(), 2)

    def test_delete_department(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo1.add_patients_to_department(repo2, department1)
        repo1.delete_department(0)
        self.assertEqual(repo1.get_size_department(), 0)

    def test_delete_all_departments(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo1.delete_all_departments()
        self.assertEqual(repo1.get_size_department(), 0)

    def test_sort_patients_by_PNC(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        repo1.add_department(department1)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo1.add_patients_to_department(repo2, department1)
        repo1.sort_patients_by_PNC(department1)
        try:
            l = department1.get_patients()
            if l.get_patient_by_index(0) == patient3 and l.get_patient_by_index(1) == patient1 and l.get_patient_by_index(2) == patient2:
                assert True
        except Exception as ex:
            assert False

    def test_sort_departments_by_number_of_patients(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 111, "flu")
        patient2 = Patients("B", "C", 234, "flu")
        patient3 = Patients("C", "D", 2, "flu")
        patient4 = Patients("E", "G", 3, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.add_patient(patient4)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        repo1.sort_departments_by_number_of_patients()
        try:
            l = repo1.get_all_departments()
            if l[0] == department3 and l[1] == department2 and l[2] == department1:
                assert True
        except Exception as ex:
            assert False

    def test_sort_patients_from_department_by_age(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("A", "B", 1991115, "flu")
        patient2 = Patients("B", "C", 2344509, "flu")
        patient3 = Patients("C", "D", 2000001, "flu")
        patient4 = Patients("E", "G", 3099809, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.add_patient(patient4)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        repo1.sort_patients_from_department_by_age(15)
        try:
            l = repo1.get_all_departments()
            if l[0] == department3 and l[1] == department2 and l[2] == department1:
                assert True
        except Exception as ex:
            assert False

    def test_sort_departments_and_patients_alphabetically(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("A", "E", 1991115, "flu")
        patient2 = Patients("B", "C", 2344509, "flu")
        patient3 = Patients("A", "A", 2000001, "flu")
        patient4 = Patients("E", "G", 3099809, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.add_patient(patient4)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        repo1.sort_patients_from_department_by_age(15)
        try:
            l = department1.get_patients().get_all()
            if l[0] == patient3 and l[1] == patient1 and l[2] == patient2:
                assert True
        except Exception as ex:
            assert False

    def search_departments_having_patients_with_a_certain_age(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("A", "E", 1991115, "flu")
        patient2 = Patients("B", "C", 2344509, "flu")
        patient3 = Patients("A", "A", 2000001, "flu")
        patient4 = Patients("E", "G", 3099809, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.add_patient(patient4)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        l = repo1.search_departments_having_patients_with_a_certain_age(30)
        try:
            if l[0] == department1 and l[1] == department2:
                assert True
        except Exception as ex:
            assert False

    def test_search_patients_who_have_a_string_in_their_names(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("Alexandru", "Elena", 1991115, "flu")
        patient2 = Patients("Bexan", "Cmm", 2344509, "flu")
        patient3 = Patients("A", "A", 2000001, "flu")
        patient4 = Patients("E", "G", 3099809, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.add_patient(patient4)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        l = repo1.search_patients_who_have_a_string_in_their_names("exan", department1)
        try:
            if l[0] == patient1 and l[1] == patient2:
                assert True
        except Exception:
            assert False

    def test_search_departments_having_patients_with_a_given_name(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("Alexandru", "Elena", 1991115, "flu")
        patient2 = Patients("Bexan", "Cmm", 2344509, "flu")
        patient3 = Patients("A", "A", 2000001, "flu")
        patient4 = Patients("Alexandru", "G", 3099809, "Zika")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo2.add_patient(patient4)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        l = repo1.search_departments_having_patients_with_a_given_name("Alexandru")
        try:
            if l[0] == department1 and l[1] == department2:
                assert True
        except Exception:
            assert False

    def test_back(self):
        repo1 = DepartmentsRepository()
        department1 = Departments(1, "flu", 4)
        department2 = Departments(2, "Zika", 3)
        department3 = Departments(3, "coma", 1)
        repo1.add_department(department1)
        repo1.add_department(department2)
        repo1.add_department(department3)
        repo2 = PatientRepository()
        patient1 = Patients("A", "E", 1991115, "flu")
        patient2 = Patients("B", "C", 2344509, "flu")
        patient3 = Patients("A", "A", 2000001, "flu")
        patient4 = Patients("E", "G", 3099809, "Zika")
        patient5 = Patients("Chira", "Maira", 83284289, "flu")
        patient6 = Patients("Anca", "Grad", 1111111, "flu")
        patient7 = Patients("Lolea", "Oana", 2345678, "flu")
        repo2.add_patient(patient1)
        repo2.add_patient(patient2)
        repo2.add_patient(patient3)
        repo1.add_patients_to_department(repo2, department1)
        repo1.add_patients_to_department(repo2, department2)
        repo1.add_patients_to_department(repo2, department3)
        #repo1.groups_of_patients_with_same_disease(department1, 2)


if __name__ == "__main__":
    unittest.main()
