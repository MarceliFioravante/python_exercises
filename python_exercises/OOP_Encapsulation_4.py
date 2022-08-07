#mechanism of hiding of data implementation
# instances variables are kept private and there is only one acess method from the outside with which we can change
# or acess this instances variables

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.__salary = None    # com double underscore variavel fica privada - private attribute
        self._salary = None   # com apenas one underscore variável continua acessivel - protected attribute
        self._num_bugs_solved = 0


    def code(self):
        self._num_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary


    # setter
    def set_salary(self, base_value):
        #check value, enforce contraints
        #if value < 1000:
         #   self._salary = 1000
        #if value > 20000:
        #self._salary = 20000
        self._salary = self._calculatre_salary(base_value)

    def _calculatre_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se = SoftwareEngineer('Max', 25)
#print(se.name, se.age)
#se.set_salary(6000)
#print(se.get_salary())

for i in range(70):
    se.code()
se.set_salary(6000)
print(se.get_salary())