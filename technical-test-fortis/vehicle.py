from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, year: int, tank_size: int, consumption: int -> None:
        self.year = year
        self.tank_size = tank_size
        self.consumption = consumption  # 5L per km -> consumption = 5
        self.is_moving = False

    @abstractmethod
    def compute_maximal_distance(self) -> int:
        ...
"""
Task 1:
Create a class Car that inherit from Vehicle
1/ Add a class constant nb_of_wheel equal to 4
2/ A Car can be created with a bool technical_inspection. Define init to match that requirement.
3/ Write the expected method with the following logic:
    - if the technical inspection is not done, the car cannot move
    - if the car is from before 2000, the theoretical maximal distance is reduced by 10%
    - if the car is from after 2010, the theoretical maximal distance is increased by 10%

Gabriel: introduce class Bike

Task 2:
Create a find_best_vehicle method that takes 2 vehicles as argument and return the one with the highest autonomy.

Task 3: 
Add some unit tests on find_best_vehicle
"""
