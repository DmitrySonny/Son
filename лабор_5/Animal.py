class Animal():
    def name(self):
        return self.name

    def age(self):
        return self.age

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animal):
    def __init__(self, name, age, description):
        super().__init__(name, age)
        self.description = description

    def __repr__(self):
        return '''
                This is zebra {}. It is {} years old.
                This is description about it: \n \t {}
               '''.format(self.name, self.age, self.description)

class Dolphin(Animal):
    def __init__(self, name, age, description):
        super().__init__(name, age)
        self.description = description

    def __repr__(self):
        return '''
                This is dolphin {}. It is {} years old.
                This is description about it: \n \t {}
               '''.format(self.name, self.age, self.description)