from money_model import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

params = {"width": 10, "height": 10, "N": range(10,500,10)}

results = mesa.batch_run(
    MoneyModel,
    parameters=params,
    iterations=5,
    max_steps=100,
    number_processes=1,
    data_collection_period=1,
    display_progress=True
)

results_df = pd.DataFrame(results)
print(results_df.head())

# I want to see how the Gini coefficient changes given the rise of the population (N)
# so I need to take the Gini value of the 100th step of any of de N agents of all 245 runs.
# I have 245 runs because N is first 10, then 20, ..., then 490 and I did 5 iterations each.
# Since I did 5 iterations, it means I will have 5 different Gini coefficients for the same N number of agents

# The final values I need are in the colummn Gini and N to create the scatterplot to view how Gini's coefficient behaved.
# Since the Gini value is the same for all agents, I can drop all the lines that don't belong to agent 0
# Select only the lines which step == 100

Gini_data = results_df.loc[(results_df['AgentID'] == 0) & (results_df['Step'] == 100)]
N_values = Gini_data.N.values
Gini_values = Gini_data.Gini.values

plt.figure()
plt.scatter(N_values, Gini_values)
plt.title("Gini's coefficient with growing of population")
plt.xlabel("N number of agents")
plt.ylabel("Gini's coefficient")




# Now I want to show, in the case in which there is 10 agents, how the wealth of EACH agent changes over time.
# I will arbitrarily pick the iteration 3
# To do this I will plot a graph with lines, each one representing one agent.

wealth_data = results_df.loc[(results_df["N"] == 10) & (results_df["iteration"] == 3)]

agents = set(wealth_data["AgentID"])

plt.figure()
for agent in agents:
    data_to_plot = wealth_data.loc[wealth_data["AgentID"] == agent]
    plt.plot(data_to_plot["Step"], data_to_plot["Wealth"], label=agent)

plt.legend()
plt.xlabel("Step")
plt.ylabel("Wealth")
plt.title("Evolution of Wealth according to Agent")
plt.show()