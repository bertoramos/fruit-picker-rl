
import numpy as np

import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

from collections import deque, namedtuple

import random

ImageSize = namedtuple('ImageSize', 'width height')

class TrainAgent:
	def __init__(self, image_size: ImageSize, n_actions: int):
		assert isinstance(image_size, ImageSize), "agent.error: image_size is not a ImageSize instance"
		assert n_actions >= 2, "agent.error: two or more actions are required"

		self.image_size = image_size
		self.n_actions = n_actions

		self.replay_memory = deque(maxlen=1000)
		self.gamma = 0.70 # discount rate
		self.epsilon = 1.0 # Exploration rate
		self.d_epsilon = 0.99

		self.model = self._model_builder()

	def _model_builder(self):
		model = Sequential()
		
		model.add(Conv2D(32, kernel_size=(3, 3),
					activation='relu',
					input_shape=(self.image_size.width, self.image_size.height, 3)
				  ))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Conv2D(64, (3, 3), activation='relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
		model.add(Flatten())
		model.add(Dense(128, activation='relu'))

		#model.add(Dropout(0.5))
		model.add(Dense(self.n_actions, activation='linear'))

		model.compile(loss='mse', optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])
		return model

	def act(self, state):
		if np.random.rand() <= self.epsilon:
			return random.randrange(self.n_actions)
		else:
			prediction = self.model.predict(state)
			return np.argmax(prediction)

	def remember(self, state, action, reward, next_state, done):
		self.replay_memory.append((state, action, reward, next_state, done))

	def replay(self, batch_size):
		if len(self.replay_memory) > batch_size:
			minibatch = random.sample(self.replay_memory, batch_size)
		else:
			minibatch = [e for e in self.replay_memory]
		for state, action, reward, next_state, done in minibatch:
			target = reward
			if not done:
				target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
				prediction = self.model.predict(state)
				prediction[0][action] = target
				self.model.fit(state, prediction, epochs=1, verbose=0)
		self.epsilon *= self.d_epsilon

	def save_model(self, file_name: str):
		self.model.save(file_name + ".h5")


	def get_exploration_rate(self):
		return self.epsilon


class PerformanceAgent:

	def __init__(self, file_name):
		self.model = load_model(file_name + ".h5")

	def act(self, state):
		prediction = self.model.predict(state)
		return np.argmax(prediction)

