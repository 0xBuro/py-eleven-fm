from .person import Person

class Coach(Person):
    def __init__(self, name, age, strategy):
        super().__init__(name, age)
        self._strategy = strategy
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, new_strategy):
        self._strategy = new_strategy
        