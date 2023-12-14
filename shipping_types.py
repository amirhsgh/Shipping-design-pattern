from interfaces import ShippingType, ShippingVehicle
from shipping_vehicles import Car, Truck, Motorcycle


class NormalShippingType(ShippingType):
    def create_vehicle(self):
        return Car()


# TODO: implement HeavyShippingType and QuickShippingType
class QuickShippingType(ShippingType):
    def create_vehicle(self):
        return Motorcycle()

class HeavyShippingType(ShippingType):
    def create_vehicle(self):
        return Truck()