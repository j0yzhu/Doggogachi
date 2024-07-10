from abc import ABC, abstractmethod

from domain import item, pet

class Player(ABC):
    @abstractmethod
    def add_pet(self, pet: pet.Pet) -> bool:
        ...

    @abstractmethod
    def remove_pet(self, pet: pet.Pet) -> bool:
        ...

    @abstractmethod
    def add_coins(self, coins: int) -> bool:
        ...

    @abstractmethod
    def remove_coins(self, coins: int) -> bool:
        ...

    @abstractmethod
    def add_item(self, item: item.Item) -> bool:
        pass

    @abstractmethod
    def remove_item(self, item: item.Item) -> bool:
        pass