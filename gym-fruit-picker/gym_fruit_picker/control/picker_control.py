
from gym_fruit_picker.elements import Position
import math


def picker_control(picker, fruit):
    picker_pos = picker.get_position()
    fruit_pos = fruit.get_position()

    picker_size = picker.get_size()
    fruit_size = fruit.get_size()

    p_a = Position(x=picker_pos.x,
                   y=picker_pos.y)
    p_b = Position(x=picker_pos.x + picker_size.width,
                   y=picker_pos.y)

    f_a = Position(x=fruit_pos.x,
                   y=fruit_pos.y - fruit_size.height)
    f_b = Position(x=fruit_pos.x + fruit_size.width,
                   y=fruit_pos.y - fruit_size.height)

    if p_a.x <= f_a.x <= p_b.x and f_a.y <= p_a.y:
        return True
    if p_a.x <= f_b.x <= p_b.x and f_b.y <= p_a.y:
        return True
    if f_a.y <= p_a.y:
        return False
    return False


def is_fruit_lost(picker, fruit):
    picker_pos = picker.get_position()
    fruit_pos = fruit.get_position()

    picker_size = picker.get_size()
    fruit_size = fruit.get_size()

    p_a = Position(x=picker_pos.x,
                   y=picker_pos.y)
    p_b = Position(x=picker_pos.x + picker_size.width,
                   y=picker_pos.y)

    f_a = Position(x=fruit_pos.x,
                   y=fruit_pos.y - fruit_size.height)
    f_b = Position(x=fruit_pos.x + fruit_size.width,
                   y=fruit_pos.y - fruit_size.height)

    return f_a.y <= p_a.y and\
           not p_a.x < f_a.x < p_b.x and\
           not p_a.x < f_b.x < p_b.x
