
from gym_fruit_picker.elements.tools import Position, Size


class Fruit:

    def __init__(self, pos0: Position, size: Size, dy: float):
        self.__pos = pos0
        self.__size = size
        self.__dy = dy

        self.__collected = False

    def move(self):
        if not self.__collected:
            x = self.__pos.x
            y = self.__pos.y
            self.__pos = Position(x, y - self.__dy)

    def collect(self):
        self.__collected = True

    def was_collected(self):
        return self.__collected

    def get_position(self):
        return self.__pos

    def get_size(self):
        return self.__size