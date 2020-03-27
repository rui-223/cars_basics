import matplotlib.pyplot as plt

class Car(object): # called by writing car.Car( , , )
    def __init__(self, position, velocity, world, color = 'r'):

        self.state = [position, velocity] # position : [y, x]; velocity : [vy, vx]
        self.world = world # 2D list
        self.color = color

        self.path = []
        self.path.append(position)

    def move(self, dt = 1):
        height = len(self.world)
        width = len(self.world[0])

        position = self.state[0]
        velocity = self.state[1]

        predicted_position = [(position[0] + velocity [0]*dt) % height, (position[1] +velocity[1]*dt) % width]

        self.state = [predicted_position, velocity]
        self.path.append(predicted_position)

    def turn_left(self): #rotates velocity, vy = -vx, vx = vy
        velocity = self.state[1]
        predicted_velocity = [-velocity[1], velocity[0]]
        self.state[1] = predicted_velocity
    def turn_right(self):
        velocity = self.state[1]
        predicted_velocity = [velocity[1], -velocity[0]]
        self.state[1] = predicted_velocity

    def display_world(self):
        position = self.state[0]
        plt.matshow(self.world, cmap = 'gray') #plot matrix into graph
        ax=plt.gca() #get current axes
        rows = len(self.world)
        cols = len(self.world[0])
        ax.set_xticks([x - 0.5 for x in range(1, cols)], minor = True) #use minor scale
        ax.set_yticks([y - 0.5 for y in range(1, rows)], minor = True)

        plt.grid(which='minor',ls='-',lw=2,color='gray') #linestyle,linewidth

        ax.text(position[1], position[0], 'x', ha = 'center', va = 'center', color = self.color, fontsize = 30)

        if(len(self.path) > 1):
            for pos in self.path:
                if(pos != position):
                    ax.text(pos[1], pos[0], '.', ha = 'center', va = 'baseline', color = self.color, fontsize = 30)
        plt.show()





