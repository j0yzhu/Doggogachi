import typing
from abc import ABC, abstractmethod
import random

if typing.TYPE_CHECKING:  # Not imported at runtime, only when type checking
    from domain import player_model, item_model, contest_model
    from typing import Optional


class Pet(ABC):
    def __init__(self, age: int, name: str):
        self._food_lvl = 100
        self._entertainment_lvl = 100
        self._age = age
        self._name = name
        self._owner = None
        self._skills = {}

    @property
    def owner(self) -> Optional[player_model.Player]:
        return self._owner

    def eat(self, item: item_model.Food) -> bool:
        self._food_lvl = max(self._food_lvl + item.food_lvl_increase, 100)
        return True

    def increase_age(self, years: int = 1) -> int:
        self._age += years
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

    def practice_skill(self, skill: str) -> bool:
        current_level = self._skills.get(skill, 0)

        # Base chance of leveling up (e.g., 80% at level 0)
        base_chance = 0.8

        # Decrease chance based on current level
        level_up_chance = base_chance / (1 + 0.1 * current_level)

        # Attempt to level up
        if random.random() < level_up_chance:
            self._skills[skill] = current_level + 1
            return True
        else:
            return False

    def calculate_skill_performance(self, skill: str) -> float:
        base_performance = random.uniform(0, 100)

        base_skill_bonus = self._skills.get(skill, 0)
        random_skill_bonus = min(base_skill_bonus * random.gauss(0.2, 1.2), 50)  # Capped to 50

        return base_performance * (1 + random_skill_bonus / 100)
