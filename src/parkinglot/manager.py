from src.parkinglot.vehicle import Vehicle


class Manager:

    def __init__(self, parkinglot_list, parking_boys):
        self.parkinglot_list = parkinglot_list
        self.parking_boys = parking_boys

    def park(self, vehicle):
        parkable = self.parkinglot_list + self.parking_boys
        for p in parkable:
            if not p.is_full():
                p.park(vehicle)

    def get_vehicle(self, ticket) -> Vehicle:
        parkable = self.parkinglot_list + self.parking_boys
        target_parkinglot = next(filter(lambda p: p.contains_vehicle(ticket), parkable),
                                 None)

        return target_parkinglot.get_vehicle()
