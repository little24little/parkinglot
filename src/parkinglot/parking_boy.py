from src.parkinglot.parking_lot import ParkingLot

from src.parkinglot.ticket import Ticket
from src.parkinglot.vehicle import Vehicle
from typing import List


class ParkingBoy:

    def __init__(self, parkinglot_list: List[ParkingLot]):
        self.parkinglot_list = parkinglot_list

    def park(self, vehicle: Vehicle) -> Ticket:
        available_parkinglot = next(
            iter((parking_lot for parking_lot in self.parkinglot_list if not parking_lot.is_full())),
            None)

        return available_parkinglot.park(vehicle)

    def get_vehicle(self, ticket: Ticket) -> Vehicle:
        target_parkinglot = next(filter(lambda p: p.contains_vehicle(ticket), self.parkinglot_list))

        return target_parkinglot.get_vehicle(ticket)

    def is_full(self):
        return len(self.parkinglot_list) == len([p for p in self.parkinglot_list if p.is_full()])


class SmartParkingBoy(ParkingBoy):

    def park(self, vehicle: Vehicle) -> Ticket:
        available_parkinglot = next(
            iter(sorted(self.parkinglot_list, key=lambda parking_lot: parking_lot.get_left(), reverse=True)),
            None
        )

        return available_parkinglot.park(vehicle)


class SuperParkingBoy(ParkingBoy):

    def park(self, vehicle: Vehicle) -> Ticket:
        available_parkinglot = next(
            iter(sorted(self.parkinglot_list, key=lambda parking_lot: parking_lot.get_empty_rate(), reverse=True)),
            None
        )

        return available_parkinglot.park(vehicle)
