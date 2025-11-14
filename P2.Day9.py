## Pendulum work simulation
# theta = degree
# g = gravity
# L = length of string

import math
import matplotlib.pyplot as plt

g = 9.81
L = 1.0
dt = 0.01
theta = math.radians(30)
omega = 0

theta_list = []
time_list = []

t = 0

for _ in range(2000):
    alpha = -(g / L) * math.sin(theta)
    omega += alpha * dt
    theta += omega * dt

    theta_list.append(theta)
    time_list.append(t)

    t += dt

plt.plot(time_list, theta_list)
plt.title("Pendulum Simulation (Euler)")
plt.xlabel("Time(S)")
plt.ylabel("Theta (rad)")
plt.grid()
plt.show()