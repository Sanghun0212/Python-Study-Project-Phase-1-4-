## Day 18 : Bicycle Model

## move direction that head looking forward
## need to use theta 

# x, y -  position
# theta - heading angle
# v - speed
# delta - steering angle

# state vector = [x, y, theta, v, delta]

# center is in rear | L = length
# x-velocity = v * cos(theta)
# y-velocity = v * sin(theta)
# angle velocity = v/L * tan(delta) 
# delta = 0 (forward) / delta > 0 (left) / delta < 0 (right)

import matplotlib.pyplot as plt
import math

dt = 0.01
L = 1.0
v = 2.0

x, y = 0.0, 0.0
theta = 0.0

x_list = []
y_list = []

for step in range(400):

    if step < 200:
        delta = 0.0
    else: 
        delta = math.radians(20)

    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += (v / L) * math.tan(delta) * dt

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.title("2D robot motion (bicycle model)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid()
plt.show()

# left - straight - right (s curve)

import matplotlib.pyplot as plt
import math

dt = 0.01
L = 1.0
v = 2.0

x, y = 0.0, 0.0
theta = 0.0

x_list = []
y_list = []

for step in range(600):

    if step < 150:
        delta = math.radians(20)
    
    elif step < 300:
        delta = 0.0

    else: 
        delta = math.radians(-20)

    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += (v / L) * math.tan(delta) * dt

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.title("2D robot motion (bicycle model)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid()
plt.show()


# random steering

import matplotlib.pyplot as plt
import math
import random

dt = 0.01
L = 1.0
v = 2.0

x, y = 0.0, 0.0
theta = 0.0

x_list = []
y_list = []

for step in range(1000):

    delta_deg = random.uniform(-30.0, 30.0)  # pull out random umbers
                                             # uniform --> all numbers collected with same percentage 
    delta = math.radians(delta_deg)

    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += (v / L) * math.tan(delta) * dt

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.title("2D robot motion (bicycle model)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid()
plt.show()

# draw circle 

import matplotlib.pyplot as plt
import math

dt = 0.01
L = 1.0
v = 2.0
r = 5.0

x, y = 0.0, 0.0
theta = 0.0
delta = math.atan(L/r)

x_list = []
y_list = []

for step in range(60000):


    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += (v / L) * math.tan(delta) * dt

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.title("2D robot motion (bicycle model)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid()
plt.show()