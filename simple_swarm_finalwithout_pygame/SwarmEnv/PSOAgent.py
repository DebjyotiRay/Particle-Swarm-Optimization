import numpy as np
import math
class PSOAgent:
    def __init__(self, idx, position):
        self.agent_id = idx
        self.position = np.array(position).astype(int)
        self.fitness_value = np.inf
        self.P_best_pos = np.array(position).astype(int)
        self.max_velocity = 20
        self.velocity = np.array((0, 0))
        
    def get_velocity(self):
        return self.velocity
        
    def get_position(self):
        return self.position
        
    def update_velocity(self, swarm):
        v_t = self.get_velocity()
                
        for i in range(0, swarm.num_dim):
            r1 = np.random.uniform(0, 1, 1)
            r2 = np.random.uniform(0, 1, 1)
            
            cog_dist = self.P_best_pos[i]-self.position[i]
            soc_dist = swarm.G_best_pos[i]-self.position[i]
            vel = swarm.inertia*v_t[i] + swarm.cognitive_weight*r1*math.sqrt(cog_dist) + swarm.social_weight*r2*math.sqrt(soc_dist)
            
            if vel > self.max_velocity:
                vel = self.max_velocity
            
            elif vel < 0:
                vel = 0
                
            self.velocity[i] = vel
            
    def update_position(self, swarm):
        print('velocity:',self.get_velocity())
        '''for i in range(0, swarm.num_dim):
            dv = self.velocity[i]
            
            pos_t = self.position[i]
            
            if i == 0:#
                if pos_t + dv < 20 or pos_t + dv > swarm.screen_width - 20:
                    dv = -dv
            else:
                if pos_t + dv < 15 or pos_t + dv > swarm.screen_height - 50:
                    dv = -dv
            
            self.position[i] = int(pos_t + dv)'''
