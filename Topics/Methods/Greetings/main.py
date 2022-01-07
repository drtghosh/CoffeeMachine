class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return f'Hello, I am {self.name}!'


name_input = input()
new_person = Person(name_input)
print(new_person.greet())