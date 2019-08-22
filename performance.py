
from agent import PerformanceAgent

import gym
import gym_fruit_picker

import numpy as np

env = gym.make('fruit-picker-v0')

agent = PerformanceAgent('model_fruit_picker')

state = env.reset()

done = False
while not done:
	action = agent.act(np.array([state]))
	state, reward, done, _ = env.step(action)
	
	env.render()
env.close()
