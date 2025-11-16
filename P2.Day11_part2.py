## Day 11 Part 2 with damping coefficient

import matplotlib.pyplot as plt

m = 1.0
k = 4.0
c_list = [0.1, 0.5, 2.0, 5.0]
dt = 0.01

for c in c_list:  ## calculate different c
    x = 1.0
    v = 0.0
    t = 0.0

    x_list = []
    time_list = []

    for _ in range(3000):
        a = -k/m * x -c/m * v
        v += a * dt
        x += v * dt
        t += dt

        x_list.append(x)
        time_list.append(t)

    plt.plot(time_list, x_list, label = f"c = {c}")

plt.title("Damped Mass-Spring with Different c")
plt.xlabel("Time(s)")
plt.ylabel("Displacement(m)")
plt.legend()
plt.grid()
plt.show()

