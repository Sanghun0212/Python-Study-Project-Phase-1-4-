## Day 16 : State Variables (moment intertia)
# rod which length is 2.0
import matplotlib.pyplot as plt
import math

m = 1.0
I = 1.0
dt = 0.01

x, y = 0.0, 0.0
vx, vy = 0.0, 0.0
theta = 0.0
omega = 0.0

Fx, Fy = 5.0, 5.0
r_x, r_y = 1.0, 2.0

x_list = []
y_list = []
theta_list = []

for _ in range(2000):

    ax = Fx / m
    ay = Fy / m

    torque = r_x * Fy - r_y * Fx

    alpha = torque / I

    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
     
    omega += alpha * dt
    theta += omega * dt

    x_list.append(x)
    y_list.append(y)
    theta_list.append(theta)

plt.plot(x_list, y_list)
plt.title("2D Rigid Body Path")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()