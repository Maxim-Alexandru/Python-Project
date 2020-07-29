class Patients:
    def __init__(self, first_name, last_name, PNC, disease):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__PNC = PNC
        self.__disease = disease

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_PNC(self):
        return self.__PNC

    def get_disease(self):
        return self.__disease

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_PNC(self, PNC):
        self.__PNC = PNC

    def set_disease(self, disease):
        self.__disease = disease

    def __str__(self):
        return "The patient " + self.get_first_name() + "  " + self.get_last_name() + ", having the personal numeric code " + str(self.get_PNC()) + ", suffers from the following diseases: " + self.get_disease()

    def __eq__(self, other):
        if self.get_PNC() == other.get_PNC():
            return True
        return False


