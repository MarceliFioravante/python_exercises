# position, name, age, level, salary
se1 = ['Software Engineer', "Max", 20, 'Junior', 5000]
se2 = ['Software Engineer', "Lisa", 25, 'Senior', 7000]

# class (blueprint)
class SoftwareEngineer:
    #pass
    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instances attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}...')

    #def information(self):
     #   information = f"Name = {self.name}, Age = {self.age}, Level = {self.level}"
      #  return information

    # dunder (double underscore) method
    def __str__(self):
        information = f"Name = {self.name}, Age = {self.age}, Level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):  #essa funcao so pode ser usada na classa Soft.Eng e nao na instance, pq nao usamos o parametro self
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000



# instance (object)
se1 = SoftwareEngineer("Max", 20, 'Junior', 5000)
#print(se1.name, se1.level)
#print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Lisa", 25, 'Senior', 7000)
se3 = SoftwareEngineer("Lisa", 25, 'Senior', 7000)

se1.code()
se2.code_in_language('Python')
print(se1)
print(se2 == se3)
#se1.entry_salary(27) # nao funciona pois serao lidos dois parametros (self, 27), mas a def so aceita um
print(SoftwareEngineer.entry_salary(27))
print(se1.entry_salary(24))  # agora funciona por causa do decorator @staticmethod