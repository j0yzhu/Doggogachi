from abc import ABC, abstractmethod

class Item(ABC):
    pass


class Food(ABC, Item):
    pass