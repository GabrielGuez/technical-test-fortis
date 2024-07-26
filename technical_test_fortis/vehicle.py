from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, year: int, tank_size: int, consumption: int) -> None:
        self.year = year
        self.tank_size = tank_size
        self.consumption = consumption  # 5L per km -> consumption = 5

    @abstractmethod
    def compute_maximal_distance(self) -> int:
        ...
