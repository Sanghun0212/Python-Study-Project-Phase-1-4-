import matplotlib.pyplot as plt

# parameters
m = 1.0
k = 4.0
c = 0.5
dt = 0.001   # intentionally larger to show difference

# acceleration function
def acceleration(x, v, k, m, c):
    return -k/m * x - c/m * v

# -------------------------------
# Euler Method
# -------------------------------
x_e = 1.0
v_e = 0.0
t_e = 0.0

x_e_list = []
t_e_list = []

for _ in range(3000):
    a_e = acceleration(x_e, v_e, k, m, c)
    v_e += a_e * dt
    x_e += v_e * dt
    t_e += dt

    x_e_list.append(x_e)
    t_e_list.append(t_e)

# -------------------------------
# RK4 Method
# -------------------------------
x_r = 1.0
v_r = 0.0
t_r = 0.0

x_r_list = []
t_r_list = []

for _ in range(3000):
    # k1
    k1_x = v_r
    k1_v = acceleration(x_r, v_r, k, m, c)

    # k2
    x_k2 = x_r + 0.5 * dt * k1_x
    v_k2 = v_r + 0.5 * dt * k1_v
    k2_x = v_k2
    k2_v = acceleration(x_k2, v_k2, k, m, c)

    # k3
    x_k3 = x_r + 0.5 * dt * k2_x
    v_k3 = v_r + 0.5 * dt * k2_v
    k3_x = v_k3
    k3_v = acceleration(x_k3, v_k3, k, m, c)

    # k4
    x_k4 = x_r + dt * k3_x
    v_k4 = v_r + dt * k3_v
    k4_x = v_k4
    k4_v = acceleration(x_k4, v_k4, k, m, c)

    # update
    x_r += dt * (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6.0
    v_r += dt * (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6.0
    t_r += dt

    x_r_list.append(x_r)
    t_r_list.append(t_r)

# -------------------------------
# Plotting Comparison
# -------------------------------
plt.plot(t_e_list, x_e_list, label="Euler", linewidth=2)
plt.plot(t_r_list, x_r_list, label="RK4", linestyle='--')

plt.title("Euler vs RK4 Comparison (Damped Mass-Spring)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.grid()
plt.show()
