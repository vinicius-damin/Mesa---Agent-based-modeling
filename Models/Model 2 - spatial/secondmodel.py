from money_model import *
import numpy as np
import matplotlib.pyplot as plt

# instantiate and run model
model = MoneyModel(50,10,10)
for i in range(100):
    model.step()


# generate grid that shows how many agents in each cell
agent_counts = np.zeros((model.grid.width, model.grid.height))

for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()
plt.title("Position of agents in the last step of the model")
plt.xlabel("X location")
plt.ylabel("Y Location")


# generate graph that shows Gini's coefficient
gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.title("Evolution of Gini's coefficient")
plt.xlabel("Step")
plt.ylabel("Gini's coefficient")


# show table with all the wealth of the agents at each step
agent_wealth = model.datacollector.get_agent_vars_dataframe()
print(agent_wealth)

# save data to csv
gini.to_csv("model_data.csv")

plt.show()