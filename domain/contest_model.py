import typing
from abc import ABC
import random

if typing.TYPE_CHECKING:
    from typing import Set
    from domain import pet_model, item_model


class Contest(ABC):
    def __init__(self, skill: str, reward_coins: int, reward_items: Set[item_model.Item]):
        self._pets: Set[pet_model.Pet] = set()
        self._skill: str = skill
        self._reward_coins: int = reward_coins
        self._reward_items: Set[item_model.Item] = reward_items
        self._winner: pet_model.Pet = None

    @property
    def skill(self):
        return self._skill

    @property
    def reward_coins(self):
        return self._reward_coins

    def add_pet(self, pet: pet_model.Pet) -> bool:
        if pet in self._pets:
            return False

        for existing_pet in self._pets:
            if existing_pet.owner == pet.owner:
                return False  # A user can only have 1 of their pets in the contest

        self._pets.add(pet)
        return True

    def remove_pet(self, pet: pet_model.Pet) -> bool:
        if pet not in self._pets:
            return False

        self._pets.remove(pet)
        return True

    def run_contest(self):
        performances = []  # (Score, Pet)

        for pet in self._pets:
            performances.append((pet.calculate_skill_performance(self._skill), pet))
            pet.practice_skill(self._skill)

        winner = max(performances)[1]  # Second element is score
        winner.owner.add_coins(self._reward_coins)
        for item in self._reward_items:
            winner.owner.add_item(item)

        self._winner = winner