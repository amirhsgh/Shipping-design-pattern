import unittest
from shipping_vehicles import Car
from shipping_types import NormalShippingType


class TestShipping(unittest.TestCase):

    def test_car_ship(self):
        car = Car()
        self.assertEqual(car.ship(), "Car shipping")

    def test_normal_shipping_type(self):
        normal_shipping = NormalShippingType()
        vehicle = normal_shipping.create_vehicle()
        self.assertIsInstance(vehicle, Car)
