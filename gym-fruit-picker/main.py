#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gym_fruit_picker.elements import Fruit, Picker, Position, Size, Action, Limit
from gym_fruit_picker.drawers import FruitDrawer, PickerDrawer
from gym_fruit_picker.control import picker_control, is_fruit_lost

from pynput.keyboard import Key, Listener

import gym
from gym.envs.classic_control import rendering

import numpy as np

try:
    VP_WIDTH = 400
    VP_HEIGHT = 400
    SCALE = 30
    FPS = 60

    WIDTH = VP_WIDTH/SCALE
    HEIGHT = VP_HEIGHT/SCALE

    viewer = rendering.Viewer(VP_WIDTH, VP_HEIGHT)
    viewer.set_bounds(0, WIDTH, 0, HEIGHT)

    fruit = Fruit(pos0=Position(x=0, y=VP_HEIGHT),
                  size=Size(width=10, height=10),
                  dy=1)

    fd = FruitDrawer(viewer, SCALE, fruit, color=(.9, .1, .1))

    picker = Picker(pos0=Position(x= int(VP_WIDTH/2), y=10),
                    dx=5,
                    size=Size(40, 10))

    pd = PickerDrawer(viewer, SCALE, picker, color=(.9, .9, .1))

    def on_press(key):
        if key == Key.left:
            picker.move(Action.LEFT, limit=Limit(top=VP_HEIGHT, bottom=0, left=0, right=VP_WIDTH))
        elif key == Key.right:
            picker.move(Action.RIGHT, limit=Limit(top=VP_HEIGHT, bottom=0, left=0, right=VP_WIDTH))

    def on_release(key):
        pass

    listener = Listener(on_press = on_press, on_release = on_release)
    listener.start()

    for _ in range(1000):
        fruit.move()
        if picker_control(picker, fruit):
            fruit.collect()

        if not fruit.was_collected() and not is_fruit_lost(picker, fruit):
            fd.draw()
        pd.draw()
        rgb = viewer.render(return_rgb_array=True)

        import time
        time.sleep(1/FPS)

finally:
    rgb = viewer.get_array()
    print(np.array([[3,3],[3,3]], dtype=np.uint8))
    print(Action(0))

    print(rgb.dtype)
    print("h -> " + str(len(rgb)))
    print("w -> " + str(len(rgb[0])))
    viewer.close()
