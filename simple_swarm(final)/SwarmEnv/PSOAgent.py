import pygame
import numpy as np

class PSOAgent:
    def __init__(self, idx, position):
        self.agent_id = idx
        self.agent_color = (255, 0, 0)
        self.agent_radius = 10
        self.position = np.array(position)
        self.fitness_value = np.inf
        self.P_best_pos = self.position
        self.velocity = np.array((0.0, 0.0))
        self.max_velocity = 20
        self.trajectory = []
        self.trajec_color = (np.random.randint(low = 0, high = 255, size = 3))
        
    def draw_agent_on_map(self, screen, WIDTH, HEIGHT):
        x = int((self.position[0] + 10) / 20 * WIDTH)
        y = int((self.position[1] + 10) / 20 * HEIGHT)
        
        self.trajectory.append((x,y))
        for i in range(len(self.trajectory)-1):
            pygame.draw.line(screen, self.trajec_color, self.trajectory[i], self.trajectory[i+1], 2)
            
        pygame.draw.circle(screen, self.agent_color, (x, y), self.agent_radius)
        
    def update_velocity(self, swarm):
        v_t = self.velocity
        
        for i in range(0, swarm.num_dim):
            r1 = np.random.uniform(0, 1, 1)
            r2 = np.random.uniform(0, 1, 1)
            
            cog_dist = self.P_best_pos[i]-self.position[i]
            soc_dist = swarm.G_best_pos[i]-self.position[i]
            
            vel = swarm.inertia*v_t[i] + swarm.cognitive_weight*r1*cog_dist + swarm.social_weight*r2*soc_dist
            
            if vel > self.max_velocity:
                vel = self.max_velocity
                
            elif vel < -self.max_velocity:
                vel = -self.max_velocity
                
            self.velocity[i] = vel
            
    def update_position(self, swarm):
        dv = self.velocity
        pos_t = self.position
        
        for i in range(0, swarm.num_dim):
            self.position[i] = pos_t[i] + dv[i]
            
