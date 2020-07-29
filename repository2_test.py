from domain.business2 import Patients
from infrastructure.repository2 import PatientRepository
import unittest


class PatientRepositoryTest(unittest.TestCase):
    def test_add_patient(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        repo.add_patient(patient1)
        self.assertEqual(repo.get_size(), 1)

    def test_get_index(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        self.assertEqual(repo.get_index(patient1), 0)

    def test_get_patient_by_index(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        self.assertEqual(repo.get_patient_by_index(0), patient1)

    def test_get_patient_by_name(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        l = []
        l.append(patient3)
        self.assertEqual(repo.get_patient_by_name("L", "P"), l)
        try:
            self.assertEqual(repo.get_patient_by_name("A", "B"), patient2)
            assert False
        except Exception as ex:
            assert True

    def test_get_patients_with_same_disease(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        patient4 = Patients("A", "B", 10101, "flu")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        repo.add_patient(patient4)
        l = []
        l.append(patient1)
        l.append(patient4)
        self.assertEqual(repo.get_patients_with_the_same_disease("flu"), l)

    def test_add_new_disease(self):
        repo = PatientRepository()
        patient1 = Patients("K", "A", 2121, "flu")
        repo.add_patient(patient1)
        repo.add_new_disease("Zika", patient1)
        self.assertEqual(patient1.get_disease(), "flu, Zika")

    def test_update_disease(self):
        repo = PatientRepository()
        patient1 = Patients("A", "B", 101, "flu")
        repo.add_patient(patient1)
        repo.update_disease("Zika", patient1)
        self.assertEqual(patient1.get_disease(), "Zika")

    def test_get_index_by_PNC(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        self.assertEqual(repo.get_index_by_PNC(patient1.get_PNC()), 0)

    def test_update_patient_by_PNC(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        patient4 = Patients("K", "AA", 2221, "...")
        repo.update_patient_by_PNC(patient4, 2221)
        try:
            if patient1 == patient4:
                assert True
        except Exception as ex:
            assert False

    def test_update_patient_by_index(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        patient4 = Patients("A", "A", 2221, "Zika")
        copy = patient2
        repo.update_patient_by_index(patient4, 2)
        try:
            if patient2 == copy:
                assert False
        except Exception as ex:
            assert True

    def test_delete_a_patient(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        repo.delete_a_patient_by_index(0)
        self.assertEqual(repo.get_size(), 2)

    def test_delete_patients_with_a_given_disease(self):
        repo = PatientRepository()
        patient1 = Patients("K", "J", 324, "flu")
        patient2 = Patients("L", "R", 2221, "Zika")
        patient3 = Patients("L", "P", 1209, "Yellow fever")
        patient4 = Patients("R", "TT", 362, "flu")
        patient5 = Patients("p", "ZZ", 1010, "flu")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        repo.add_patient(patient4)
        repo.add_patient(patient5)
        repo.delete_patients_with_a_given_disease("flu")
        self.assertEqual(repo.get_size(), 2)

    def test_delete_patient_by_PNC(self):
        repo = PatientRepository()
        patient1 = Patients("A", "AA", 111, "flu")
        patient2 = Patients("B", "BB", 124, "flu")
        patient3 = Patients("C", "L", 90, "Zika")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        repo.delete_patient_by_PNC(90)
        self.assertEqual(repo.get_size(), 2)

    def test_delete_all_patients(self):
        repo = PatientRepository()
        patient1 = Patients("A", "AA", 111, "flu")
        patient2 = Patients("B", "BB", 124, "flu")
        patient3 = Patients("C", "L", 90, "Zika")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        repo.delete_all_patients()
        self.assertEqual(repo.get_size(), 0)

    def test_delete_patients_from_a_given_interval(self):
        repo = PatientRepository()
        patient1 = Patients("A", "AA", 111, "flu")
        patient2 = Patients("B", "BB", 124, "flu")
        patient3 = Patients("C", "L", 90, "Zika")
        patient4 = Patients("D", "C", 10101, "Denger fever")
        patient5 = Patients("E", "E", 9101, "Zika")
        repo.add_patient(patient1)
        repo.add_patient(patient2)
        repo.add_patient(patient3)
        repo.add_patient(patient4)
        repo.add_patient(patient5)
        repo.delete_patients_from_a_given_interval(1, 3)
        self.assertEqual(repo.get_size(), 2)


if __name__ == "__main__":
    unittest.main()
