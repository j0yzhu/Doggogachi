from abc import ABC, abstractmethod

from domain import items, pets
from typing import List

class Player(ABC):
    @abstractmethod
    def add_pet(self, pet: pets.Pet) -> bool:
        ...

    @abstractmethod
    def remove_pet(self, pet: pets.Pet) -> bool:
        ...

    @abstractmethod
    def add_coins(self, coins: int) -> bool:
        ...

    @abstractmethod
    def remove_coins(self, coins: int) -> bool:
        ...

    @abstractmethod
    def add_item(self, item: items.Item) -> bool:
        pass

    @abstractmethod
    def remove_item(self, item: items.Item) -> bool:
        pass


class PlayerImpl(Player):

    def __init__(self):
        self._pet_list: List[pet.Pet]