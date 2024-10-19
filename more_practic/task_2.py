from datetime import date

class Person:
    def __init__(self, name:str, country:str, data_of_birth:date):
        self.name = name
        self.country = country
        self.data_of_birth = data_of_birth
    

    def get_сurrent_date(self):
        return date.today()
    
    def get_age(self):
        today = self.get_сurrent_date()
        age = today.year - self.data_of_birth.year
        check_data = date(today.year, self.data_of_birth.month, self.data_of_birth.day)
        if today <  check_data:
            age -= 1
        return age
    

