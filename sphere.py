
import numpy as np
import matplotlib.pyplot as plt

def main():
    width = 100
    height = 100
    coord_x = []
    coord_y = []
    
    # x, y coordinate
    for x in range(width):
        for y in range(height):
            coord_x.append(-width/2 + x)# formula for scaling and bringing down the projection from 3d to 2d
            coord_y.append(-height/2 + y)# ek side mein jo global optimum tham, usse kheenchkar beech mein laya gaya through transformation
    
    max_x = max(coord_x)
    min_x = min(coord_x)
    max_y = max(coord_y)
    min_y = min(coord_y)
    
    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    
    # x, y values
    x = np.arange(min_x, max_x, 1)
    y = np.arange(min_y, max_y, 1)
    
    # x,y grid
    X, Y = np.meshgrid(x, y)
    
    # Sphere function
    Z = (X*X)+(Y*Y)

    surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)
    
    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('f(x,y)', labelpad=20)

    fig.colorbar(surf, shrink=0.5, aspect=8)
    
    plt.show()
        
if __name__ == '__main__':
    main()	
