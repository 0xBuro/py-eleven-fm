from .person import Person
import random 

class Player(Person):
    def __init__(self, name, age, position, number, skill):
        super().__init__(name, age)
        self.position = position
        self.number = number
        self.skill = skill
    
    def shoot(self):
        shoot_skill = random.uniform(0, self.skill)
        return shoot_skill