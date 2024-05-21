class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000
    power = 1000

    def hourse_power(self, power):
        return power

class Nissan(Car, Vehicle):
    prise = 200000
    vehicle_type = "Rio"

    def __init__(self, car_number):
        self.car_number = car_number

    def __str__(self):
        return self.car_number

    def hourse_power(self, power):
        return power


Mashina = Nissan(car_number='AA000A')
print(Mashina)
print(Mashina.vehicle_type)
print(Mashina.prise)
print(Mashina.hourse_power(2000))