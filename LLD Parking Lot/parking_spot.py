from colorama import Fore, Back, Style

from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_num: int):
        self._id = spot_num
        self.spots_vehicle_type = VehicleType.CAR # default spot type is car
        self.parked_vehicle = None
    
    # getters
    def get_id(self): return self._id
    def get_spots_vehicle_type(self) -> VehicleType: return self.spots_vehicle_type
    def get_parked_vehicle(self) -> Vehicle:
        if self.parked_vehicle: return self.parked_vehicle
        else: return None
    
    def isAvailable(self) -> bool:
        return self.parked_vehicle is None
    
    def park_vehicle(self, vehicle: Vehicle) -> None:
        print(Fore.WHITE)
        try:
            if not self.isAvailable():
                raise Exception(Fore.RED + "[ERROR]: This Spot is already Occupied")
            
            if self.spots_vehicle_type != vehicle.get_type():
                raise Exception(Fore.RED + "[ERROR]: The vehicle type will not be able to park in this spot")
            
            # normally: All good, park the vehicle
            self.parked_vehicle = vehicle
            print(f"{Vehicle} parked.")
            print(Style.RESET_ALL)
            
        except Exception as e:
            return e
        
        return
    
    def unpark_vehicle(self) -> None:
        print(Fore.WHITE)
        try:
            if self.isAvailable():
                raise Exception(Fore.RED + "[ERROR]: This Spot is Empty")
            
            # normally: All good, clear the spot
            self.parked_vehicle = None
            print(f"{self._id} is now empty.")
            print(Style.RESET_ALL)
        
        except Exception as e:
            return e
        
        return
         
            