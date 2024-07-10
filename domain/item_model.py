from abc import ABC, abstractmethod


class Item(ABC):
    pass


class Food(ABC, Item):
    def __init__(self, food_lvl_increase: int):
        self.food_lvl_increase: int = food_lvl_increase


class Kibble(Food):
    def __init__(self):
        super().__init__(30)


class Meat(Food):
    def __init__(self):
        super().__init__(50)


class Vegetable(Food):
    def __init__(self):
        super().__init__(10)


class Fruit(Food):
    def __init__(self):
        super().__init__(10)