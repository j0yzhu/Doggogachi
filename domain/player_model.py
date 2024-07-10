import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:  # Not imported at runtime, only when type checking
    from domain import pet_model, item_model
    from typing import Set


class Player:
    def __init__(self):
        self._pets: Set[pet_model.Pet] = set()
        self._coins = 0
        self._items: Set[item_model.Item] = set()

    @property
    def pets(self) -> Set[pet_model.Pet]:
        return self._pets

    @property
    def coins(self) -> int:
        return self._coins

    @property
    def items(self) -> Set[item_model.Item]:
        return self._items

    def add_pet(self, pet: pet_model.Pet) -> bool:
        if pet in self._pets:
            return False

        if pet.owner is not None and pet.owner != self:
            return False

        self._pets.add(pet)
        pet.owner = self
        return True

    def remove_pet(self, pet: pet_model.Pet) -> bool:
        if pet not in self._pets:
            return False

        self._pets.remove(pet)
        pet.owner = None
        return True

    def add_coins(self, coins: int) -> bool:
        self._coins += coins
        return True

    def remove_coins(self, coins: int) -> bool:
        if coins > self._coins:  # If the user doesn't have enough coins
            return False

        self._coins -= coins
        return True

    def add_item(self, item: item_model.Item) -> bool:
        if item in self._items:
            return False

        self._items.add(item)
        return True

    def remove_item(self, item: item_model.Item) -> bool:
        if item not in self._items:
            return False

        self._items.remove(item)
        return True

    def feed(self, pet: pet_model.Pet, food: item_model.Food) -> bool:
        if pet not in self.pets or food not in self.items:
            return False

        if not pet.eat(food):  # If the pet isn't hungry
            return False

        self._items.remove(food)
        return True
