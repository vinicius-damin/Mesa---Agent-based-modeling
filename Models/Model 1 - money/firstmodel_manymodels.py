import matplotlib.pyplot as plt
from money_model import *

all_wealth = []

for i in range(100):
    # Instantiate the model
    model = MoneyModel(10)

    # runs the model
    for j in range(10):
        model.step()

    # store the results
    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)

plt.hist(all_wealth, bins=range(max(all_wealth)+1))
plt.show()