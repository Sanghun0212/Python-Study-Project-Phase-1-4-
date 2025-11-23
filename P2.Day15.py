## Day 15 : 2D Particle Dynamics
# Create Dynamic model in 2D plate

import matplotlib.pyplot as plt

m = 1.0
dt = 0.01
g = 9.81

x, y = 0.0, 0.0
vx, vy = 5.0, 10.0


x_list = []
y_list = []

for _ in range(2000):
    Fx = 0
    Fy = - m * g    


    ax = Fx / m
    ay = Fy / m

    vx += dt * ax
    vy += dt * ay

    x += dt * vx
    y += dt * vy

    if y < 0:
        break

    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.title("Projectile Morion(2D)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()

## Advance code

import matplotlib.pyplot as plt

m = 1.0
dt = 0.01
g = 9.81

positions = [     # Set 3 different positions to compare 3 different cases
    [0.0, 0.0],   # positions[0] = first case
    [0.0, 0.0],   # positions[1] = second case
    [0.0, 0.0]    # positions[2] = third case
]

velocities = [    # same logic with positions
    [0.0, 10.0],
    [5.0, 5.0],
    [10.0, 10.0]
]

path_x = [[], [], []]
path_y = [[], [], []]

for _ in range(2000):

    Fx = 0
    Fy = -m * g

    ax = Fx / m
    ay = Fy / m

    for i in range(3):              # repeat 3 times with 3 different cases

        velocities[i][0] += ax * dt              # Standard form to indicate 2D vectors
        velocities[i][1] += ay * dt              # [0] - x / [0] - y

        positions[i][0] += velocities[i][0] * dt
        positions[i][1] += velocities[i][1] * dt

        if positions[i][1] < 0:     # this line mean : if position y goes under 0, stop this loop and continue to append values in the path
            continue

        path_x[i].append(positions[i][0])
        path_y[i].append(positions[i][1])

plt.plot(path_x[0], path_y[0], label="vy=10")
plt.plot(path_x[1], path_y[1], label="vx=5, vy=5")
plt.plot(path_x[2], path_y[2], label="vx=10, vy=10")

plt.title("Projectile Motion Comparisons")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()