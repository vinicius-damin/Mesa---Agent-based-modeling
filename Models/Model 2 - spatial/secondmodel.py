from money_model import *
import numpy as np
import matplotlib.pyplot as plt

model = MoneyModel(50,10,10)
for i in range(20):
    model.step()


# grid that shows how many agents in each cell
agent_counts = np.zeros((model.grid.width, model.grid.height))

for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()
plt.show()

