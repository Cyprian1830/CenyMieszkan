from src.zajecia04.personnel.driver import Driver
from src.zajecia04.fleet.ambulance import Ambulance
from src.zajecia04.personnel.employee import Employee


class Station:

    __slots__ = ['id', 'location', 'ambulance', 'driver', 'additional_employee']

    def __init__(self, id: int, location: str, ambulance: Ambulance,
                 driver: Driver, additional_employee: Employee):
        self.location = location
        self.id = id
        self.ambulance = ambulance
        self.driver = driver
        self.additional_employee = additional_employee

    def is_ambulance_on_the_right_place(self):
        if self.ambulance.location == self.location:
            print("Ambulance on the right place!")
        else:
            print("Ambulance on the wrong place!")


stacja = Station(1, "Krakow",
                 Ambulance('car', 'ready', 'Krakow', '10/10'),
                 Driver("Cyprian", "Szot", 1, 8000, 123, "very good"),
                 Employee("Kazimierz", "Szwedow", 123, 5600, ))
