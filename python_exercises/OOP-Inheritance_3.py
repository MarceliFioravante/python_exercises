# processo em que uma classe pega os atributos e metodos de outra classe
# essa nova classe é chamada de Child Class e a classe inicial é chamada de Parent Class


# inherits, extend, override
class Employee:   #Parent Class

    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working...')

class SoftwareEngenieer(Employee):  #Child class

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)    #comando para usar os dados que ja estao na parent class
        self.level = level

    def debug(self):
        print(f'{self.name} is debugging...')

    def work(self):                                 #se usar essa def work, ele nao vai usar a def work do parent (override)
        print(f'{self.name} is coding...')

class Designer(Employee):

    def draw(self):
        print(f'{self.name} is drawing...')

    def work(self):                                #se essa def for retirada, esse classa passa a usar a def work do parent.
        print(f'{self.name} is designing...')

se = SoftwareEngenieer('Max', 25, 6000, 'Junior')
#print(se.name, se.age)
#se.work()
#se.debug()
d = Designer('Marceli', 31, 7000)
#print(d.name, d.age)
#d.work()
#d.draw()


#Polymorphism - programas that work with the supper class but also with any subclass as well.

employees = [SoftwareEngenieer('Max', 25, 6000, 'Junior'),
             SoftwareEngenieer('Lisa', 30, 9000, 'Junior'),
             Designer('Marceli', 31, 7000)]

def motivate_employees(employees):
    for employees in employees:
        employees.work()

motivate_employees(employees)

# Recap:
# Inheritance: ChildClass(BaseClass)
# inherit attributes and functions, extend attributes and functions and override functionalities
# supper().__init__ - if we override the __init__ in a childClass, remember to call the Supper method of the baseClass