from interfaces import ShippingVehicle


class Car(ShippingVehicle):
    def ship(self):
        return "Car shipping"


class Truck(ShippingVehicle):
    def ship(self):
        return "Truck shipping"
    

class Motorcycle(ShippingVehicle):
    def ship(self) -> str:
        return "Motorcycle shipping"
