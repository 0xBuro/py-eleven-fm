from .person import Person

class Manager(Person):
    def __init__(self, name, age, club=None):
        super().__init__(name, age)
        self._club = club
           
    @property
    def club(self):
        return self._club
    
    @club.setter
    def club(self, new_club):
        self._club = new_club