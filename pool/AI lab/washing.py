import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables and membership functions
wash_load = ctrl.Antecedent(np.arange(0, 11, 1), 'wash_load')
dirt_percentage = ctrl.Antecedent(np.arange(0, 101, 1), 'dirt_percentage')
wash_time = ctrl.Consequent(np.arange(0, 101, 1), 'wash_time')

# Define membership functions for wash load
wash_load['small'] = fuzz.trimf(wash_load.universe, [0, 0, 5])
wash_load['medium'] = fuzz.trimf(wash_load.universe, [0, 5, 10])
wash_load['large'] = fuzz.trimf(wash_load.universe, [5, 10, 10])

# Define membership functions for dirt percentage
dirt_percentage['low'] = fuzz.trimf(dirt_percentage.universe, [0, 0, 50])
dirt_percentage['medium'] = fuzz.trimf(dirt_percentage.universe, [0, 50, 100])
dirt_percentage['high'] = fuzz.trimf(dirt_percentage.universe, [50, 100, 100])

# Define membership functions for wash time
wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 0, 50])
wash_time['medium'] = fuzz.trimf(wash_time.universe, [0, 50, 100])
wash_time['long'] = fuzz.trimf(wash_time.universe, [50, 100, 100])

# Define rules based on fuzzy logic
rule1 = ctrl.Rule(wash_load['small'] & dirt_percentage['low'], wash_time['short'])
rule2 = ctrl.Rule(wash_load['medium'] & dirt_percentage['medium'], wash_time['medium'])
rule3 = ctrl.Rule(wash_load['large'] & dirt_percentage['high'], wash_time['long'])

# Create a control system and simulate
wash_time_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
washing_machine = ctrl.ControlSystemSimulation(wash_time_ctrl)

# Example usage with user input
user_wash_load = float(input("Enter wash load (0-10): "))
user_dirt_percentage = float(input("Enter dirt percentage (0-100): "))

washing_machine.input['wash_load'] = user_wash_load
washing_machine.input['dirt_percentage'] = user_dirt_percentage

washing_machine.compute()

# Output the result
print("Estimated wash time:", washing_machine.output['wash_time'], "minutes")