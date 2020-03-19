class Person:
    def __init__(self, age, name, salary=0):
        self.person_age = age
        self.person_name = name
        self.salary = salary

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

    def func(self):
        print('Person', self.__class__.__name__, self)


class Manager(Person):
    def __init__(self):
        Person.__init__(self, 1, 'Manager', -1)     # super().__init__(1, 'Manager', -1)  # Равносильно
        self.new_attr = 0

    def func(self, a1, a2):
        return m.__str__


m = Manager()  # 43, 'John'
m.func(1, 2)
print(str(m), repr(m), m.__dict__, sep='\n')
