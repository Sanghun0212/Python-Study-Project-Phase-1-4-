## Day 17 - collision

# perfectly elastic = collision 
# perfectly inelastic = stick after collision

# coefficient of retitution (e)
# e = after velocity / before velocity  |  perfectly elastic = 1 / perfectly inelastic = 0

# Set the wall
# x = 0,1 / y = 0,1

# import matplotlib.pyplot as plt

# dt = 0.01

# x, y = 0.5, 0.5 
# vx, vy = 2.0, 1.0

# x_list = []
# y_list = []

# for _ in range(3000):

#     x += vx * dt
#     y += vy * dt

#     # Collision with vertical walls
#     if x <= 0 or x >1:
#         vx *= -1

#     # Collision with horizontal walls
#     if y <= 0 or y >1:
#         vy *= -1

#     x_list.append(x)
#     y_list.append(y)

# plt.plot(x_list, y_list)
# plt.title("2D Ball Bouncing in a Box")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid()
# plt.show()


## Use reflection Vector equationm
# v' = v-2(v * n)n    v = current velocity vector  n = normalized normal vector
# ex) 45 degree wall --> normal = (-root(2)/2, root(2)/2)
# if wall is 45 degrees and x = y
# y > x --> area of upper line
# y = x --> line
# y < x --> area of under line
# when y < x --> collision occur

import numpy as np
import matplotlib.pyplot as plt

dt = 0.01

x, y = 0.5, 0.2
vx, vy = 1.5, 2.0

# np --> NumPy : standard library of math and science calculation
# L use NumPy for calculating matrix

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a + b) --> [5, 7, 9]
# print(a * 2) --> [2, 4, 6]
# print(np.dot(a,b)) --> 1 * 4 + 2 * 5 + 3 * 6 = 32

n = np.array([1.0, -1.0])
n = n / np.linalg.norm(n)

# n reflects size of direction source
# length of n need to be always 1 so v cannot effect size of their value but effect on direction
# np.linalg.norm(n) --> find length of the vector in (_)

x_list, y_list = [], []

for _ in range(2000):
    x += vx * dt
    y += vy * dt

    if y < x :
        v = np.array([vx, vy])
        v_reflect = v - 2 * np.dot(v, n) * n

        vx, vy = v_reflect[0], v_reflect[1]

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.title("Bounce Off Slanted Wall(y=x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()