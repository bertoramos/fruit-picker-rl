
from enum import Enum

from gym_fruit_picker.elements.tools import Position, Size, Limit


class Action(Enum):
    LEFT = 0
    RIGHT = 1
    NOTHING = 2


class Picker:

    def __init__(self, pos0: Position, dx: float, size: Size):
        assert isinstance(pos0, Position), "picker.error : pos0 must be a Point instance"
        assert dx > 0, "picker.error : dx must be non-zero positive"
        assert isinstance(size, Size), "picker.error : size must be a Size instance"
        assert size.height > 0 and size.width > 0, "picker.error : size must be non-zero positive"

        self.__pos = pos0
        self.__dx = dx
        self.__size = size

    def move(self, action: Action, limit: Limit):
        assert isinstance(action, Action), "picker.error : action must be an Action instance"
        assert isinstance(limit, Limit), "picker.error : limit must be a Limit instance"
        assert limit.top > limit.bottom, "picker.error : top must be greater than bottom"
        assert limit.left < limit.right, "picker.error : left must be lower than bottom"

        assert limit.left <= self.__pos.x <= limit.right - self.__size.width, "picker.error : x position must be between left and right limit"
        assert limit.bottom + self.__size.height <= self.__pos.y <= limit.top, "picker.error : y position must be between top and bottom limit"

        x = self.__pos.x
        y = self.__pos.y

        # Realizar acción
        if action == Action.LEFT and limit.left <= x - self.__dx:
            x -= self.__dx
            self.__pos = Position(x, y)
        elif action == Action.RIGHT and x + self.__size.width + self.__dx <= limit.right:
            x += self.__dx
            self.__pos = Position(x, y)

    def get_position(self):
        return self.__pos

    def get_size(self):
        return self.__size
