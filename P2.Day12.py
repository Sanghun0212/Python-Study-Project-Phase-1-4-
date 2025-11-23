## Day 12 Runge-Kutta 4( RK4 )
## This make more detail on slope
import matplotlib.pyplot as plt

m = 1.0
k = 4.0
c = 0.5
dt = 0.01

x = 1.0
v = 0.0
t = 0.0

x_list = []
time_list = []

def acceleration(x, v, k, m, c):
    return -k/m * x -c/m * v

for _ in range(3000):

    ## k#_x is a slope of position = velocity
    ## k#_v is a slope of velocity = acceleration
    
    ## Current Starting point (k1)
    k1_x = v
    k1_v = acceleration(x, v, k, m, c)

    ## First Half of step point (k2)
    x_k2 = x + 0.5 * dt * k1_x
    v_k2 = v + 0.5 * dt * k1_v
    k2_x = v_k2
    k2_v = acceleration(x_k2, v_k2, k, m, c)

    ## Second Half of step point (k3)
    x_k3 = x + 0.5 * dt * k2_x
    v_k3 = v + 0.5 * dt * k2_v
    k3_x = v_k3
    k3_v = acceleration(x_k3, v_k3, k, m, c)
    
    ## Fully Stepped (k4)
    x_k4 = x + dt * k3_x
    v_k4 = v + dt * k3_v
    k4_x = v_k4
    k4_v = acceleration(x_k4, v_k4, k, m, c)

    x += dt * (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6.0
    v += dt * (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6.0

    t += dt

    x_list.append(x)
    time_list.append(t)

plt.plot(time_list, x_list, label="RK4")
plt.title("Damped Mass-Spring System (RK4)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.grid()
plt.legend()
plt.show()
     