from SwarmEnv.PSOEnv import PSOEnv


def main():
    swarm = PSOEnv(3, 0.002, 0.001, 1.0)
    epoch = 0
    while swarm.running:
        if not swarm.convergence_criteria:
            for i in range(swarm.no_agents):
                curr_pos = swarm.PSOAgents[i].get_position()
                value = swarm.objective_function(curr_pos)
                
                if value < swarm.PSOAgents[i].fitness_value:
                    swarm.PSOAgents[i].fitness_value = value
                    swarm.PSOAgents[i].P_best_pos = curr_pos
            
            swarm.G_best_pos, swarm.G_best_val, swarm.G_best_id = swarm.find_global_best()
            
            for i in range(swarm.no_agents):
                swarm.PSOAgents[i].update_velocity(swarm)
                print('velocity:',swarm.PSOAgents[i].get_velocity())
                #swarm.PSOAgents[i].update_position(swarm)
                
            print('EPOCH:', epoch)
            [print('Agent',i,':', swarm.PSOAgents[i].position, 'Fitness Value:',swarm.PSOAgents[i].fitness_value, 'Velocity:', swarm.PSOAgents[i].velocity) for i in range(swarm.no_agents)]
            print('Global Best Agent: Agent', swarm.G_best_id)
            print('Global Best Position:', swarm.G_best_pos)
            print('Global Best Fitness Value:',swarm.G_best_val)
            print('=================================================')
        
        epoch += 1

if __name__ == '__main__':
    main()
