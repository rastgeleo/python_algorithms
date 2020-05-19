import numpy as np
from math import sin, cos, pi

rad = (-45) * (pi/180)
cos_v = cos(rad)
sin_v = sin(rad)

original = np.zeros((10,10), int)
result = np.zeros((10,10), int)
np.fill_diagonal(original, 1)

center = original.shape[0] / 2
x_center = y_center = center

width = original.shape[1]
height = original.shape[0]

copied = []
for x in range(height):
    for y in range(width):
        new_x = int(round(cos_v*(x-x_center) - sin_v*(y-y_center) + x_center))
        new_y = int(round(sin_v*(x-x_center) + cos_v*(y-y_center) + y_center))
        
        if (new_x > 0 and new_x < height) and (new_y > 0 and new_y < width):
            print('moving {} at [{}][{}] to [{}],[{}]'.format(original[x][y], x, y,new_x,new_y))
            result[new_x][new_y] = original[x][y]   # result[2][0] = original[0][0]:1
            copied.append((new_x, new_y))

print(original)
print(result)

