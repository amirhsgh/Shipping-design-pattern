from abc import ABC, abstractmethod


class ShippingVehicle(ABC):
    @abstractmethod
    def ship(self) -> str: ...


class ShippingType(ABC):
    @abstractmethod
    def create_vehicle(self) -> ShippingVehicle: ...
