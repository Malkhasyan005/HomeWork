class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("James", 25)
person2 = Person("Alice", 19)
person3 = Person("Jack", 23)

persons = [person1, person2, person3]

for person in persons:
    print(person.name, person.age)