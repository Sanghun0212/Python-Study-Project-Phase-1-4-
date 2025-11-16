### Day 11 Mass-Spring System

import matplotlib.pyplot as plt

m = 1.0
k = 4.0
dt = 0.01

# initial conditions
x1 = 1.0     # first mass initial displacement
v1 = 0.0

x2 = 0.5     # second mass initial displacement
v2 = 0.0

t = 0.0

x1_list = []
x2_list = []
time_list = []

for _ in range(3000):
    # system 1
    a1 = -k/m * x1
    v1 += a1 * dt
    x1 += v1 * dt

    # system 2
    a2 = -k/m * x2
    v2 += a2 * dt
    x2 += v2 * dt

    t += dt

    x1_list.append(x1)
    x2_list.append(x2)
    time_list.append(t)

plt.plot(time_list, x1_list, label="x0 = 1.0 m")
plt.plot(time_list, x2_list, label="x0 = 0.5 m")
plt.title("Mass-Spring (no damping, different initial displacement)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement x (m)")
plt.legend()
plt.grid()
plt.show()