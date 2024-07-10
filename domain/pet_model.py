import typing
from abc import ABC, abstractmethod
import random

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
        self._entertainment_lvl = 100
        self._age = age
        self._name = name
        self._owner = None
    @property
    def owner(self) -> player_model.Player:
        return self._owner

    def eat(self, item: item_model.Food) -> bool:
        self._food_lvl = max(self._food_lvl + item.food_lvl_increase, 100)
        return True

    def increase_age(self, years: int = 1) -> int:
        self.age += years
        return years

    def dig(self) -> None:
        """
        Randomly picks one of the following to do:

        Dig up nothing
        Dig up coins
        Dig up an item

        If it digs up coins it's added to the owners coins
        If it digs up an item it's added to the owners items
        :return:
        """


    def play(self) -> None:
        """
        2 Options we can have here:

        1. Have a toy Item - Similar to food where it defines how much to increase entertainment level by
        2. Just refill the entertainment level when the owner players with it
        :return:
        """
