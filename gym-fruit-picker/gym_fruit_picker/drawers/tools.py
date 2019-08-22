
from gym_fruit_picker.elements.tools import Position


def transform(position: Position, scale):
    x = position.x / scale
    y = position.y / scale

    return Position(x, y)
