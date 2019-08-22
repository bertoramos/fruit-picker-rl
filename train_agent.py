
import gym
import gym_fruit_picker

from agent import TrainAgent, ImageSize

import numpy as np

env = gym.make('fruit-picker-v0')

train_agent = TrainAgent(ImageSize(200, 200), 3)

epochs = 300
batch_size = 500

for epoch in range(epochs):
	done = False

	prev_state = np.array([env.reset()])
	while not done:
		action = train_agent.act(prev_state)
		current_state, reward, done, _ = env.step(action)
		current_state = np.array([current_state])
		env.render()
        
		train_agent.remember(prev_state, action, reward, current_state, done)
        
		prev_state = current_state
	train_agent.replay(batch_size)
	print("\n\n----------\n EPOCH " + str(epoch+1) + "/" + str(epochs) +" \n----------\n" + 
			" Reward : " + str(reward) + "\n" + 
			" Exploration rate : " + str(train_agent.get_exploration_rate()) + "\n")
env.close()
train_agent.save_model("model_fruit_picker")
