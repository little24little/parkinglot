from src.parkinglot.ticket import Ticket
from src.parkinglot.vehicle import Vehicle


class ParkingLot:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.room = {}

    def park(self, vehicle: Vehicle):
        if self.is_full():
            raise NoEnoughRoomError
        ticket = Ticket(vehicle)
        self.room[ticket] = vehicle

        return ticket

    def is_full(self) -> bool:
        return len(self.room) >= self.capacity

    def get_vehicle(self, ticket: Ticket) -> Vehicle:
        return self.room.pop(ticket)

    def contains_vehicle(self, ticket: Ticket) -> bool:
        return ticket in self.room

    def get_left(self) -> int:
        return self.capacity - len(self.room)

    def get_empty_rate(self) -> float:
        return self.get_left() / len(self.room) if len(self.room) else 0


class NoEnoughRoomError(Exception):

    def __init__(self, *args, **kwargs):
        pass
