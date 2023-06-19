import random
from .person import Person

class Goalkeeper(Person):
    def __init__(self, name, age, number, reflex):
        super().__init__(name, age)
        self.position = 'TW'
        self.number = number
        self.reflex = reflex
    
    def parry(self):
        reflex_skill = random.uniform(0, self.reflex)
        return reflex_skill