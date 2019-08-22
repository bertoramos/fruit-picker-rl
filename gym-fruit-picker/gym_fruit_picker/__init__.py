from gym.envs.registration import register

register(
    id='fruit-picker-v0',
    entry_point='gym_fruit_picker.envs:FruitPickerEnv',
)
