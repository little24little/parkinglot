from unittest import TestCase

from src.parkinglot.parking_lot import ParkingLot
from src.parkinglot.vehicle import Vehicle


class TestParkingLot(TestCase):

    def test_park_car_is_full(self):
        parking_lot = ParkingLot(1)
        vehicle = Vehicle('A123123')
        parking_lot.park(vehicle)

        self.assertTrue(parking_lot.is_full())
