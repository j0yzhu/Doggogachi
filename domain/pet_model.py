import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:  # Not imported at runtime, only when type checking
    from domain import player_model, item_model


class Pet(ABC):
    @property
    @abstractmethod
    def owner(self) -> player_model.Player:
        pass

    @owner.setter
    @abstractmethod
    def owner(self, player: player_model.Player) -> None:
        ...

    @abstractmethod
    def eat(self, item: item_model.Food) -> bool:
        pass

    @abstractmethod
    def increase_age(self, years: int = 1) -> int:
        pass

    @abstractmethod
    def dig(self) -> None:
        pass

    @abstractmethod
    def play(self) -> None:
        pass


class PetImpl(Pet):
    def __init__(self, age: int, name: str):
        self._food_lvl = 100
        self._age = age
        self._name = name
        self._owner = None
    @property
    def owner(self) -> player_model.Player:
        return self._owner

    def eat(self, item: item_model.Food) -> bool:
        if isinstance(item, item_model.Food):



    def increase_age(self, years: int = 1) -> int:
        self.age += years

    def dig(self) -> None:
        pass

    def play(self) -> None:
        pass