import matplotlib.pyplot as plt

class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __repr__(self):
        plt.imshow([[(self.r / 255, self.g / 255, self.b / 255)]])
        plt.show([[(self.r / 255, self.g / 255, self.b / 255)]])
        #plt.imshow([[(self.r/255, self.g/255, self.b/255)]])
        string = 'rgb = [{}, {}, {}]'.format(self.r, self.g, self.b)

        return string
    def __add__(self, other):
        new_r = (self.r + other.r) / 2
        new_g = (self.g + other.g) / 2
        new_b = (self.b + other.b) / 2
        return Color(new_r, new_g, new_b)

