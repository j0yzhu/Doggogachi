from abc import ABC, abstractmethod
from domain import items


class Pet(ABC):
    @abstractmethod
    def eat(self, item: inventory_item.Food) -> bool:
        ...

    @abstractmethod
    def increase_age(self, years: int = 1) -> int:
        ...

    @abstractmethod
    def dig(self) -> None:
        ...

    @abstractmethod
    def play(self) -> None:
        ...
