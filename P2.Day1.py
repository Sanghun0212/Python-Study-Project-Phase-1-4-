## 20250131 Python
import matplotlib.pyplot as plt

## import(불러오기)_matplotlib(라이브러리 이름).pyplot(하위 모듈) as pit(pit 로 부를께 라는 뜻)
# 그냥 import matplot 이라고 하면되는데 뒤에 py.plot이라고 붙인 이유는 그래프용 도구만 쓰려고 한것

# initial conditions
v0 = 50     # initial speed(m/s)
angle = 45  # launch angle(degree)
g = 9.81    # gravity (m/s^2)
k = 0.02    # drag coefficient
dt = 0.01   # time step(S)
m = 1       # mass(kg)

# convert degree to radian

vx = v0 * math.cos(math.radians(angle))
vy = v0 * math.sin(math.radians(angle))

#lists to store trajectory
x_list, y_list = [0],[0]

# initialize positions
x, y = 0, 0

while y >=0:    # loop until projectile hits the ground
    v = math.sqrt(vx**2 + vy**2)
    ax = -(k/m) * v * vx
    ay = -g - (k/m) * v * vy

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    x_list.append(x)
    y_list.append(y)

pit.plot(x_list, y_list)
pit.title("Projectile Motion with Air resistence")
pit.xlabel("Horizontal Distance(m)")
pit.ylabel("Height (m)")
pit.grid(True)
pit.show()
