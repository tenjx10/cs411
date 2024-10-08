from typing import Optional, List

from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat

class HabitatManager:
    def __init__(self) -> None:
        habitats: dict[int, Habitat] = {}

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def remove_habitat(self, habitat_id: int) -> None:
        pass

    def get_habitats_by_geographic_area(self, geographic_area: str) -> List[Habitat]:
        pass

    def get_habitats_by_size(self, size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(self, environment_type: str) -> List[Habitat]:
        pass

    def get_habitat_by_id(self, habitat_id: int) -> Habitat:
        pass

    def assign_animals_to_habitat(self, habitat_id: int, animals: List[Animal]) -> None:
        pass






