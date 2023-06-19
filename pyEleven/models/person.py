import datetime as dt

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age    

    def get_name(self):
        return self.name

    def get_ageFromBirthday(self):
        if isinstance(self.age, int):
            return self.age
        else: 
            today = dt.date.today()
            age = today.year - self.age.year
            
            if today.month < self.age.month or (today.month == self.age.month and today.day < self.age.day):
                age -= 1
            return age     