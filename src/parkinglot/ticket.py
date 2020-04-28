import datetime

from src.parkinglot.vehicle import Vehicle


class Ticket:

    def __init__(self, vehicle: Vehicle):
        self.car_num = vehicle.car_num
        self.timestamp = datetime.datetime.now()
