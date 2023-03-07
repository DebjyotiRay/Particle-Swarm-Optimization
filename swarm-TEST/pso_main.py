from PSOEnv import PSOEnv
from PSOAgent import PSOAgent


def main():
    swarm = PSOEnv(3, 0.002, 0.001, 1.0)#number_of_agents ,inertia, cognitive weight, social weight
    #cognitive weight gives the current based location; and its coordinates/
    #social weight gives the 

    epoch = 0
    while swarm.running:
        # swarm.event_on_game_window()
        print("EPOCH ", epoch)
        if not swarm.convergence_criteria:
            for i in range(swarm.no_agents):
                curr_pos = swarm.PSOAgents[i].get_position()
                print("CURRENT POSITION UNDER SWARM RUNNING ", curr_pos)
                value = swarm.objective_function(curr_pos)
                
                if value < swarm.PSOAgents[i].fitness_value:
                    swarm.PSOAgents[i].fitness_value = value
                    swarm.PSOAgents[i].P_best_pos = curr_pos
                    
            swarm.G_best_pos, swarm.G_best_val, swarm.G_best_id = swarm.find_global_best()
            
            for i in range(swarm.no_agents):

                swarm.PSOAgents[i].trajectory.append(curr_pos)
                swarm.PSOAgents[i].update_velocity(swarm)
                swarm.PSOAgents[i].update_position(swarm)
                print('Agent',i,': ', swarm.PSOAgents[i].position)
               
            epoch += 1
        #swarm.view()
    
if __name__ == '__main__':
    main()
