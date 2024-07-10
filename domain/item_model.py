from abc import ABC, abstractmethod

class Item(ABC):
    pass


class Food(ABC, Item):
    def __init__(self, hunger_reduction: int):
        self.hunger_reduction: int = hunger_reduction


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