## Day2 Python
# Compare 2cases (Case 1 : no air resistance / Case2 : with air resistance )
#1
import matplotlib.pyplot as plt
import math


v0 = 50     # initial speed (m/s)
angle = 45  # launch angle (deg)
g = 9.81    # gravity(m/s^2)
k = 0.001    # air resistance coefficient
dt = 0.01   # time step(s)
m = 1       # mass(kg)

vx0 = v0 * math.cos(math.radians(angle))
vy0 = v0 * math.sin(math.radians(angle))

# Case 1: without air resistance

x1, y1 = 0, 0
vx1, vy1 = vx0, vy0
x_list1, y_list1 = [0], [0]

while y1 >= 0:
# using "+=" to make Euler Integration System --> acceleration - velocity - position

    vy1 += -g*dt 
    x1 += vx1 * dt                      
    y1 += vy1 * dt
    x_list1.append(x1)
    y_list1.append(y1)


# Case 2: with air resistance

x2, y2 = 0, 0
vx2, vy2 = vx0, vy0
x_list2, y_list2 = [0], [0]

while y2>= 0:
    v = math.sqrt(vx2**2 + vy2**2)
    ax = -(k/m) * v * vx2
    ay = -g - (k/m) * v * vy2
    vx2 += ax * dt 
    vy2 += ay * dt
    x2 += vx2 * dt
    y2 += vy2 * dt
    x_list2.append(x2)
    y_list2.append(y2)

plt.plot(x_list1, y_list1, label="No Air Resistance", color = "blue")   # plot ideal projectile
plt.plot(x_list2, y_list2, label="With Air Resistance", color = "red") # plot drag case

plt.title("Projectile Motion Comparison")               # fix typo
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.legend()                                            # show legend
plt.grid(True)

plt.savefig("projectile_comparison.png", dpi=300, bbox_inches="tight")  # consistent name
plt.show()


## github code
# Markdown manage the size of tile with number of "#"
# # Title
# ## Subtitle
# ### Section

# Decorate Text
# **Something** --> bold size
# _something_ --> tilt 
# ~~something~~ --> cancel line

# Link connect
# [Text You Want to show](link address)

# List
# use - 
# 1. 