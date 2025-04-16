from typing import List 
from colorama import Fore, Back, Style
from parking_spot import ParkingSpot
from vehicle import Vehicle

class Level:
    def __init__(self, floor: int, num_spots: int):
        self._id = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(1,num_spots+1)]
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.isAvailable() and spot.getType() == vehicle.getType():
                spot.park_vehicle(vehicle)
                print(f"[Level]: parked {vehicle} at {self._id}-{spot._id}")
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.isisAvailable() and spot.get_parkedVehicle() == vehicle:
                spot.unpark_vehicle()
                print(f"[Level]: {vehicle} left parking {self._id}-{spot._id}")
                return True
        return False
    
    def getAvailabilityReport() -> str:
        print(Fore.WHITE + f"Level {self._id} Availability:")
        for spot in self.parking_spots:
            if spot.isAvailable():
                print(f"Spot {spot.get_spot_number()} is "+ Back.GREEN +"AVAILABLE")
            else:
                print(f"Spot {spot.get_spot_number()} is "+ Back.RED +"NOT AVAILABLE")
        print(Style.RESET_ALL)
                