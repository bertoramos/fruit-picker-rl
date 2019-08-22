
import gym
import gym_fruit_picker

env = gym.make('fruit-picker-v0')

try:
    for _ in range(2):
        done = False
        env.reset()
        while not done:
            img, reward, done, _ = env.step(env.action_space.sample())

            env.render()
        print(reward)
except:
	pass
finally:
	env.close()
