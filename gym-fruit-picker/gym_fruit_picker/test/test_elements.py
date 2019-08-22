
import unittest

from gym_fruit_picker.elements.picker import Picker, Action
from gym_fruit_picker.elements.tools import Position, Size, Limit

from gym_fruit_picker.elements.fruit import Fruit


class PickerTest(unittest.TestCase):

    def setUp(self) -> None:
        self._width = 100
        self._height = 100
        picker_width = 20
        picker_height = 10
        self._picker = Picker(pos0=Position(x=0, y=15),
                              dx=1,
                              size=Size(width=picker_width, height=picker_height))

    def test_move_left_limit(self):
        for _ in range(1000):
            self._picker.move(action=Action.LEFT, limit=Limit(0, self._height, 0, self._width))
        self.assertTrue(self._picker.get_position() == Position(x=0, y=15))

    def test_move_right_limit(self):
        for _ in range(1000):
            self._picker.move(action=Action.RIGHT, limit=Limit(0, self._height, 0, self._width))
        self.assertTrue(self._picker.get_position() == Position(x=100 - self._picker.get_size().width, y=15))

    def test_move(self):
        self._picker.move(action=Action.RIGHT, limit=Limit(0, self._height, 0, self._width))
        self.assertTrue(self._picker.get_position() == Position(x=1, y=15))
        self._picker.move(action=Action.RIGHT, limit=Limit(0, self._height, 0, self._width))
        self.assertTrue(self._picker.get_position() == Position(x=2, y=15))

        self._picker.move(action=Action.LEFT, limit=Limit(0, self._height, 0, self._width))
        self.assertTrue(self._picker.get_position() == Position(x=1, y=15))
        self._picker.move(action=Action.LEFT, limit=Limit(0, self._height, 0, self._width))
        self.assertTrue(self._picker.get_position() == Position(x=0, y=15))


class FruitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.width = 100
        self.height = 100
        x = 0
        y = self.height
        self.fruit = Fruit(pos0=Position(x=x, y=y),
                           size=Size(10, 10),
                           dy=1)

    def test_move(self):
        self.assertTrue(self.fruit.get_position().y == self.height and \
                        self.fruit.get_position().x == 0)
        self.fruit.move()

        self.assertTrue(self.fruit.get_position().y == self.height - 1 and \
                        self.fruit.get_position().x == 0)

        for _ in range(10):
            self.fruit.move()
        self.assertTrue(self.fruit.get_position().y == self.height - 11 and \
                        self.fruit.get_position().x == 0)

    def test_was_collected(self):
        self.fruit.collect()
        self.assertTrue(self.fruit.was_collected())
        self.fruit.move()
        self.assertTrue(self.fruit.get_position().y == self.height and \
                        self.fruit.get_position().x == 0)