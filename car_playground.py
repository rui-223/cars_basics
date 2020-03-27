import numpy as np
import car
import color

height = 4
width = 6
world = np.zeros((height, width))

initial_position = [0, 0]
velocity = [0, 1]
carla = car.Car(initial_position, velocity, world) #initialize car objects
carla.move()
carla.move()
carla.move()
carla.turn_left()
carla.display_world()

position2 = [2, 2]
velocity2 = [1, 0]
jeannette = car.Car(position2, velocity2,world, 'y')
jeannette.move()
jeannette.move()
jeannette.turn_left()
jeannette.move()
jeannette.turn_left()
jeannette.move()
jeannette.move()
jeannette.display_world()


color1 = color.Color(250, 0, 0)
print(color1)
color2 = color.Color(0, 50, 200)
print(color2)

new_color = color1 + color2
print(new_color)