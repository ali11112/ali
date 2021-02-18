import random

class Animal(object):

    def __init__(self, name):
        self.name = name
class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(["Doberman", "Alman köpegi", "Kangal","Buldog"])

    def fetch(self,  thing):
        print("%s goes afte the %!" %(self.name, thing))
d = Dog("dogname")
print(d.name)
print(d.breed)

