from unittest import TestCase

from src.parkinglot.parking_boy import SmartParkingBoy, ParkingBoy, SuperParkingBoy
from src.parkinglot.parking_lot import ParkingLot
from src.parkinglot.vehicle import Vehicle


class TestParkingBoy(TestCase):

    def test_parking_boy_parking(self):
        parking_lot_1 = ParkingLot(capacity=3)
        parking_lot_2 = ParkingLot(capacity=5)

        vehicle = Vehicle('A1212')

        parking_boy = ParkingBoy([parking_lot_1, parking_lot_2])
        ticket = parking_boy.park(vehicle)

        self.assertTrue(parking_lot_1.contains_vehicle(ticket))

    def test_smart_parking_boy_parking(self):
        parking_lot_1 = ParkingLot(capacity=3)
        parking_lot_2 = ParkingLot(capacity=5)

        vehicle = Vehicle('A1212')

        smart_parking_boy = SmartParkingBoy([parking_lot_1, parking_lot_2])
        ticket = smart_parking_boy.park(vehicle)

        self.assertFalse(parking_lot_1.contains_vehicle(ticket))
        self.assertTrue(parking_lot_2.contains_vehicle(ticket))

    def test_super_parking_boy_parking(self):
        parking_lot_1 = ParkingLot(capacity=3)
        parking_lot_2 = ParkingLot(capacity=5)

        vehicle = Vehicle('A1212')
        parking_lot_1.park(vehicle)
        parking_lot_2.park(vehicle)

        super_parking_boy = SuperParkingBoy([parking_lot_1, parking_lot_2])
        ticket = super_parking_boy.park(vehicle)

        self.assertFalse(parking_lot_1.contains_vehicle(ticket))
        self.assertTrue(parking_lot_2.contains_vehicle(ticket))
