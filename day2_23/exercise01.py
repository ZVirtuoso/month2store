"""
类的继承
"""


class Car():
    def __init__(self, brand: str, speed: int):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return "这是%s品牌的车"%self.brand


class ElectricVehicle(Car):
    def __init__(self, b, s, battery_capacity, charging_efficiency):
        self.speed = 42
        self.battery_capacity = battery_capacity
        super().__init__(b, s)
        self.charging_efficiency = charging_efficiency


xiaoniao = ElectricVehicle("小鸟", 40, 5, 2)
print(xiaoniao.__dict__)

print(xiaoniao)