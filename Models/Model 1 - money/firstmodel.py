from money_model import *
import matplotlib.pyplot as plt

model = MoneyModel(10)
for i in range(10):
    model.step()
  

agents_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agents_wealth)
plt.show()

# How to code with more lines the same thing
#agents_wealth = []
#for b in model.schedule.agents:
#    print(f"ID: {b.unique_id},  Wealth: {b.wealth}")
#    agents_wealth.append(b.wealth)
