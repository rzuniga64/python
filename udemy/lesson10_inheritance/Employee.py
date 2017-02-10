class Employee:

    def __init__(self, name, pay_rate):
        self.name = name
        self.pay_rate = pay_rate

    def __str__(self):
        return self.name + ", " + str(self.pay_rate)

    def pay(self, hours_worked):
        return self.pay_rate * hours_worked


class Manager(Employee):

    def __init__(self, name, pay_rate, is_salaried):
        Employee.__init__(self, name, pay_rate)
        self.salaried = is_salaried

    def __str__(self):
        ret_str = Employee.__str__(self)
        ret_str += " salaried: " + str(self.salaried)
        return ret_str

    def pay(self, hours_worked):
        if self.salaried:
            return self.pay_rate
        else:
            return self.pay_rate * hours_worked

e1 = Employee("John Jones", 10.00)
print(e1)
print("Gross pay: " + str(e1.pay(40)))
m1 = Manager("Jane Smith", 1200, True)
print(m1)
print("Gross pay: " + str(m1.pay(40)))
m2 = Manager("Jim Brown", 20.00, False)
print(m2)
print("Gross pay: " + str(m2.pay(40)))
