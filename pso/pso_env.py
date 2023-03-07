import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 640, 480
N_PARTICLES = 50
N_DIMENSIONS = 2
MAX_ITERATIONS = 100
MAX_VELOCITY = 10
GOAL_POSITION = np.array([WIDTH/2, HEIGHT/2])#declaring the goal position here, which stays constant for the entire time of the algorithm.
GOAL_RADIUS = 10
C1 = 1
C2 = 1

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Swarm Optimization")

# Define particle class
class Particle:
    def __init__(self, position):
        self.position = np.array(position)#numpy array is beingh initialized with dimension that iof the position
        self.velocity = np.zeros(N_DIMENSIONS)
        self.best_position = np.array(position)
        self.best_fitness = np.inf
    
    def update_position(self):
        self.position += self.velocity
        # Ensure particles stay within screen bounds
        self.position = np.clip(self.position, [0,0], [WIDTH, HEIGHT])
    
    def update_velocity(self, global_best_position):
        r1, r2 = np.random.rand(2)
        cognitive_component = C1 * r1 * (self.best_position - self.position)
        social_component = C2 * r2 * (global_best_position - self.position)
        self.velocity += cognitive_component + social_component
        # Ensure velocity does not exceed maximum
        self.velocity = np.clip(self.velocity, -MAX_VELOCITY, MAX_VELOCITY)
    
    def update_fitness(self):
        distance_to_goal = np.linalg.norm(self.position - GOAL_POSITION)
        if distance_to_goal < self.best_fitness:
            self.best_fitness = distance_to_goal
            self.best_position = self.position
    
    def draw(self):
        pygame.draw.circle(screen, (255,0,0), self.position.astype(int), 5)#the tuple passed is the RGB value. #
        #.astype(int) converts all individual elements of array to integer data type.

#list = [(int)item for item in list]


# Initialize particles
particles = [Particle(np.random.rand(2) * [WIDTH, HEIGHT]) for _ in range(N_PARTICLES)]#check the output of random.rand()
global_best_position = np.inf * np.ones(N_DIMENSIONS)


# Run particle swarm optimization
for iteration in range(MAX_ITERATIONS):
    # Update global best position
    for particle in particles:
        if particle.best_fitness < np.linalg.norm(global_best_position - GOAL_POSITION):
            global_best_position = particle.best_position
    
    # Update particles
    for particle in particles:
        particle.update_velocity(global_best_position)
        particle.update_position()
        particle.update_fitness()
        particle.draw()
    
    # Draw goal position and radius
    pygame.draw.circle(screen, (0,255,0), GOAL_POSITION.astype(int), GOAL_RADIUS)#this code defines goal position and global optimum is defined initially and the goal position remains constant throughout the time.
    
    # Update screen
    pygame.display.flip()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
