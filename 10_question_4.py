class BankAccount:
    def __init__(self, name, deposit):
        self.name = name
        self.deposit = int(deposit)

    def withdraw(self, amount):
        if self.deposit < amount:
            return print("Not Enough Funds")
        self.deposit -= int(amount)
        return print("Success")


class Student:
    student_count = 0

    def __init__(self, name, id):
        self.name = name
        self.id = int(id)
        Student.student_count += 1

    @classmethod
    def get_total_student(cls):
        return Student.student_count

    
    pass

class Car():
    def __init__(self, make, model, year, odom = 0):
        self.make = make
        self.model = model
        self.year = int(year)
        self.odom = int(odom)

    def drive(self, miles):
        self.odom += miles
        print(f"This car have driven {self.odom}")


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size, odom=0):
        super().__init__(make, model, year, odom)
        self.battery_size = int(battery_size)

    def describe_battery(self):
        print("This battery Size is", self.battery_size)

    def get_range(self):
        print(f"This car has a range of {self.battery_size * 4}")
    pass


alice_bank = BankAccount("Alice", 2000)
alice_bank.withdraw(200)
alice_bank.withdraw(1200)
alice_bank.withdraw(800)

print("\n\n#################")

alice = Student("Alice", 2425601)
sam = Student("Sam", 2425623)
chun_hoe = Student("Chun Hoe", 2425601)
print(Student.get_total_student())

print("\n\n#################")

build_dream = ElectricCar("BYD", "Atto", 2026, 75)
build_dream.drive(100)
build_dream.drive(800)
build_dream.describe_battery()
build_dream.get_range()