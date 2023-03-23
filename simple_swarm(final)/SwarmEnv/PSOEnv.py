import pygame
import numpy as np

from SwarmEnv.PSOAgent import PSOAgent

class PSOEnv:
    def __init__(self, n, W, C1, C2):
        pygame.init()
        self.num_dim = 2
        self.no_agents = n
        self.screen_height, self.screen_width = 600, 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.map = pygame.image.load('map.png')
        self.caption = pygame.display.set_caption("Particle Swarm Optimization")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.game_speed = 30
        self.PSOAgents = [PSOAgent(i, np.random.uniform(-10, -5, 2)) for i in range(self.no_agents)]
        self.inertia = W
        self.cognitive_weight = C1
        self.social_weight = C2
        self.G_best_pos = (0, 0)
        self.G_best_val = np.inf
        self.G_best_id = None
        self.running = True
    
    def objective_function(self, position):
        x = position[0]
        y = position[1]
        return x**2 + y**2
    
    def find_global_best(self):
        min_val = self.PSOAgents[0].fitness_value
        min_id = self.PSOAgents[0].agent_id
        min_pos = self.PSOAgents[0].position
        for agent in self.PSOAgents:
            if min_val > agent.fitness_value:
                min_val = agent.fitness_value
                min_id = agent.agent_id
                min_pos = agent.position
                
        return min_pos, min_val, min_id
                
    def event_on_game_window(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def view(self):
        self.screen.blit(self.map, (0, 0))
        for agent in self.PSOAgents:
            agent.draw_agent_on_map(self.screen, self.screen_width, self.screen_height)
            
        pygame.display.flip()
        pygame.image.save(self.screen, "pso_sphere.png")
        self.clock.tick(self.game_speed)
