
import gym
from gym.envs.classic_control import rendering

from gym_fruit_picker.elements.fruit import Fruit
from gym_fruit_picker.drawers.tools import transform
from gym_fruit_picker.elements.tools import Position


class FruitDrawer:

    def __init__(self, viewer: rendering.Viewer, scale, fruit: Fruit, color):
        self.__viewer = viewer
        self.__scale = scale
        self.__fruit = fruit
        self.__color = color

    def draw(self):
        x = self.__fruit.get_position().x
        y = self.__fruit.get_position().y
        self.__viewer.draw_polygon(v=[transform(Position(x, y), self.__scale),
                                      transform(Position(x + self.__fruit.get_size().width, y), self.__scale),
                                      transform(Position(x + self.__fruit.get_size().width, y - self.__fruit.get_size().height), self.__scale),
                                      transform(Position(x, y - self.__fruit.get_size().height), self.__scale)],
                                   filled=True, color=self.__color)
