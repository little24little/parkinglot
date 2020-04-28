import uuid
from dataclasses import dataclass


def manager_park(all_parkinglot_list, vehicle, strategy):
    """
    :param all_parkinglot_list:
    An example:

        [
            ('normal' , parkinglot_list1),
            ('left_sensitive', parkinglot_list2),
            ('empty_rate_priority', parkinglot_list3),
        ]

    :param vehicle:
    :param strategy:
    :return:
    """
    if strategy == 's1':
        for description, parkable_list in all_parkinglot_list:
            if description == 'normal':
                for parkinglot in parkable_list:
                    if not parkinglot.is_full():
                        return parkinglot.park(vehicle)

            elif description == 'left_sensitive':
                available_parkinglot = next(
                    iter(sorted(parkable_list, key=calculate_left, reverse=True)),
                    None)

                if available_parkinglot is not None:
                    return available_parkinglot.park(vehicle)

            elif description == 'empty_priority':
                available_parkinglot = next(
                    iter(sorted(parkable_list, key=calculate_empty_rate, reverse=True)),
                    None)

                if available_parkinglot is not None:
                    return available_parkinglot.park(vehicle)

    elif strategy == 's2':
        for description, parkable_list in all_parkinglot_list.reverse():
            if description == 'normal':
                for parkinglot in parkable_list:
                    if not parkinglot.is_full():
                        return parkinglot.park(vehicle)

            elif description == 'left_sensitive':
                available_parkinglot = next(
                    iter(sorted(parkable_list, key=calculate_left)), None)

                if available_parkinglot is not None:
                    return available_parkinglot.park(vehicle)

            elif description == 'empty_priority':
                available_parkinglot = next(
                    iter(sorted(parkable_list, key=calculate_empty_rate, reverse=True)),
                    None)

                if available_parkinglot is not None:
                    return available_parkinglot.park(vehicle)
    elif strategy == 's3':
        # TODO
        pass


def calculate_empty_rate(parking_lot):
    return parking_lot.get_empty_rate()


def calculate_left(parking_lot):
    return parking_lot.get_left()


@dataclass
class Vehicle:
    car_num: str


@dataclass
class Ticket:
    ticket_num: str = str(uuid.uuid4())


class ParkingLot:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.room = {}

    def park(self, vehicle: Vehicle):
        if len(self.room) >= self.capacity:
            raise NoEnoughRoomError

        ticket = Ticket()
        self.room[ticket] = vehicle

        return ticket

    def get_vehicle(self, ticket: Ticket) -> Vehicle:
        return self.room.pop(ticket)

    def get_left(self) -> int:
        return self.capacity - len(self.room)

    def get_empty_rate(self) -> float:
        return self.get_left() / len(self.room)


class NoEnoughRoomError(Exception):

    def __init__(self, *args, **kwargs):
        pass
