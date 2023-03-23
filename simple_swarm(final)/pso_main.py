from SwarmEnv.PSOEnv import PSOEnv

def main():
    swarm = PSOEnv(6, 0.5, 0.01, 1.0)
    epoch = 0
    while swarm.running:
        swarm.event_on_game_window()
        if epoch < 100:
            for agent in swarm.PSOAgents:
                curr_pos = agent.position
                value = swarm.objective_function(curr_pos)
                
                if value < agent.fitness_value:
                    agent.fitness_value = value
                    agent.P_best_pos = curr_pos
                    
            swarm.G_best_pos, swarm.G_best_val, swarm.G_best_id = swarm.find_global_best()
            
            for agent in swarm.PSOAgents:
                agent.update_velocity(swarm)
                agent.update_position(swarm)
                
        swarm.view()
                
if __name__ == '__main__':
    main()
