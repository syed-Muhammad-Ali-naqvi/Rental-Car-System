
## Models

from abc import ABC, abstractmethod
from utils import console

############
# Class Car
############
class Car:
    def __init__(self, car_id, model, brand, year, rent, available=0):
        self.car_id = str(car_id).strip()
        self.model = str(model).strip()
        self.brand = str(brand).strip()
        self.year = str(year).strip()
        try:
            self.rent = int(str(rent).strip())
        except:
            self.rent = 0
            console.print(f"[yellow]⚠️ Invalid rent for Car ID '{self.car_id}', defaulting to 0.[/yellow]")
        try:
            self.available = int(str(available).strip())
        except:
            self.available = 0
            console.print(f"[yellow]⚠️ Invalid available count for Car ID '{self.car_id}', defaulting to 0.[/yellow]")

    def to_dict(self):
        return {
            "Car ID": self.car_id,
            "Model": self.model,
            "Brand": self.brand,
            "Year": self.year,
            "Rent Per Day": str(self.rent),
            "Available": str(self.available)
        }

##############
# Class Person
#############
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def menu(self):
        pass