class Person:

    def __init__(self, first, middle, last, age):
        self.first = first
        self.middle = middle
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last + \
               ' ' + str(self.age)

    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]

    def set_first(self, first):
        self.first = first

    def set_middle(self, middle):
        self.middle = middle

    def set_last(self, last):
        self.last = last

    def set_age(self, age):
        self.age = age

person1 = Person('Jane', 'Q', 'Doe', 27)
person2 = Person('Bob', 'M', 'Smith', 55)
print(person1)
print(person2)
person1.set_age(23)
print(person1)
print(person1.initials())
