import mesa

class MoneyAgent(mesa.Agent):
    """ an agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        #This is the agent's step
        if self.wealth == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth +=1
        self.wealth -= 1
        # print(f"Hi, I am agent {str(self.unique_id)} and I have {str(self.wealth)} USD.")

class MoneyModel(mesa.Model):
    """ A model with n number of agents"""

    def __init__(self, N):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        """Advance the model by only one step"""
        self.schedule.step()

#empty_model = MoneyModel(10)
#empty_model.step()
#print('terminei')