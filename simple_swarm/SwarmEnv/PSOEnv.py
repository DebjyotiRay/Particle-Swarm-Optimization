import numpy as np

from SwarmEnv.PSOAgent import PSOAgent

class PSOEnv:
    def __init__(self, n, w, c1, c2, dim = 2):
        self.num_dim = dim
        self.no_agents = n
        self.screen_height, self.screen_width = 600, 1000
        self.PSOAgents = [PSOAgent(i, np.random.rand(2) * [self.screen_height, self.screen_width]) for i in range(self.no_agents)]
        self.inertia = w
        self.cognitive_weight = c1
        self.social_weight = c2
        self.G_best_pos = np.array((0, 0))
        self.G_best_val = np.inf
        self.G_best_id = None
        self.convergence_criteria = False
        self.running = True
        
    def objective_function(self, position):
        x = -self.screen_width/2 + position[0]
        y = -self.screen_height/2 + position[1]
        return x**2 + y**2
        
    def find_global_best(self):
        min_val = self.PSOAgents[0].fitness_value
        min_id = self.PSOAgents[0].agent_id
        min_pos = self.PSOAgents[0].position
        for i in range(1, self.no_agents):
            if min_val > self.PSOAgents[i].fitness_value:
                min_val = self.PSOAgents[i].fitness_value
                min_id = self.PSOAgents[i].agent_id
                min_pos = self.PSOAgents[i].position
                
        return min_pos, min_val, min_id
