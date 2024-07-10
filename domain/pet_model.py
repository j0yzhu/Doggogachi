import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:  # Not imported at runtime, only when type checking
    from domain import player_model, item_model


class Pet(ABC):
    @property
    @abstractmethod
    def owner(self) -> player_model.Player:
        ...

    @owner.setter
    @abstractmethod
    def owner(self, player: player_model.Player) -> None:
        ...

    @abstractmethod
    def eat(self, item: item_model.Food) -> bool:
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
