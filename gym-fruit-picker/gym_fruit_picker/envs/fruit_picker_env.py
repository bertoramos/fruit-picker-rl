
import gym
from gym.envs.classic_control import rendering

import numpy as np

from gym_fruit_picker.elements import Fruit, Picker, Action, Position, Limit, Size
from gym_fruit_picker.drawers import FruitDrawer, PickerDrawer
from gym_fruit_picker.control import picker_control, is_fruit_lost

class FruitPickerEnv(gym.Env):

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 60
    }

    def __init__(self):
        # screen
        self.world_width = 200
        self.world_height = 200
        self.scale = 40

        self.setup()

        # env
        self.action_space = gym.spaces.Discrete(3) # 0 = LEFT; 1 = RIGHT; 2 = NOTHING;

        low = np.array([[ [0, 0, 0] for _ in range(self.world_width)] for _ in range(self.world_height)], dtype=np.uint8)
        high = np.array([[ [255, 255, 255] for _ in range(self.world_width)] for _ in range(self.world_height)], dtype=np.uint8)

        self.observation_space = gym.spaces.Box(low=low,
                                                high=high)

    def setup(self):
        self.viewer = rendering.Viewer(self.world_width, self.world_height)
        self.viewer.set_bounds(0, self.world_width / self.scale, 0, self.world_height / self.scale)

        # world

        self.fruit = Fruit(pos0=Position(x=50, y=self.world_height),
                           size=Size(width=10, height=10),
                           dy=3)

        self.picker = Picker(pos0=Position(x=int(self.world_width / 2), y=10),
                             dx=8,
                             size=Size(40, 10))
        self.fd = FruitDrawer(self.viewer, self.scale, self.fruit, color=(.9, .1, .1))
        self.pd = PickerDrawer(self.viewer, self.scale, self.picker, color=(.9, .9, .1))

    def step(self, action):
        action_enum = Action(action)
        self.fruit.move()
        self.picker.move(
            action=action_enum,
            limit=Limit(top=self.world_height, bottom=0, left=0, right=self.world_width)
        )

        if picker_control(self.picker, self.fruit):
            self.fruit.collect()

        if self.fruit.was_collected():
            reward = 100
        else:
            if is_fruit_lost(self.picker, self.fruit):
                reward = -1
            else:
                reward = 0
        done = is_fruit_lost(self.picker, self.fruit) or self.fruit.was_collected()

        return self.viewer.get_array(),\
               int(reward),\
               done,\
               {'rgb uint8 np.array(shape=(' + str(self.world_height) + "," +
                                                str(self.world_width) + "," +
                                                str(3) + '))'}

    def reset(self):
        self.viewer.close()
        self.setup()
        return self.viewer.get_array()

    def render(self, mode='human'):
        self.fd.draw()
        self.pd.draw()
        self.viewer.render()

    def close(self):
        self.viewer.close()
