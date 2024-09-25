import numpy as np
import matplotlib.pyplot as plt

dt1 = 0.05
dt2 = 0.01
dt3 = 0.005
t_max = 10 * np.pi

t_0 = 0
x_0 = 0
v_0 = 1

t1, t2, t3, x1, x2, x3, v1, v2, v3, ax1, ax2, ax3, av1, av2, av3 = [t_0], [t_0], [t_0], [x_0], [x_0], [x_0], [v_0], [v_0], [v_0], [x_0], [x_0], [x_0], [v_0], [v_0], [v_0]

while abs(t1[-1] - t_max) > dt1 / 2:
    t_new = t1[-1] + dt1
    
    x_new = x1[-1] + dt1 * v1[-1]
    v_new = v1[-1] - dt1 * x1[-1]
    
    x_imp = x1[-1] + 0.5 * dt1 * (v1[-1] + v_new)
    v_imp = v1[-1] - 0.5 * dt1 * (x1[-1] + x_new)
    
    t1.append(t_new)
    
    x1.append(x_imp)
    v1.append(v_imp)
    
    ax_new = np.sin(t_new)
    ax1.append(ax_new)
    
    av_new = np.cos(t_new)
    av1.append(av_new)

while abs(t2[-1] - t_max) > dt2 / 2:
    t_new = t2[-1] + dt2
    
    x_new = x2[-1] + dt2 * v2[-1]
    v_new = v2[-1] - dt2 * x2[-1]
    
    x_imp = x2[-1] + 0.5 * dt2 * (v2[-1] + v_new)
    v_imp = v2[-1] - 0.5 * dt2 * (x2[-1] + x_new)
    
    t2.append(t_new)
    
    x2.append(x_imp)
    v2.append(v_imp) 
    
    ax_new = np.sin(t_new)
    ax2.append(ax_new)
    
    av_new = np.cos(t_new)
    av2.append(av_new)
    
while abs(t3[-1] - t_max) > dt3 / 2:
    t_new = t3[-1] + dt3
    
    x_new = x3[-1] + dt3 * v3[-1]
    v_new = v3[-1] - dt3 * x3[-1]
    
    x_imp = x3[-1] + 0.5 * dt3 * (v3[-1] + v_new)
    v_imp = v3[-1] - 0.5 * dt3 * (x3[-1] + x_new)
    
    t3.append(t_new)
    
    x3.append(x_imp)
    v3.append(v_imp)
    
    ax_new = np.sin(t_new)
    ax3.append(ax_new)
    
    av_new = np.cos(t_new)
    av3.append(av_new)    

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].plot(t1, x1, label='h = 0.05', color='tab:blue')
ax[0].plot(t2, x2, label='h = 0.01', color='tab:orange')
ax[0].plot(t3, x3, label='h = 0.005', color='tab:green')
ax[0].plot(t1, ax1, '--', label='a', color='black')

ax[0].set_xlabel('t')
ax[0].set_ylabel('x(t)')
ax[0].legend()

ax[1].plot(t1, v1, label='h = 0.05')
ax[1].plot(t2, v2, label='h = 0.01')
ax[1].plot(t3, v3, label='h = 0.005')
ax[1].plot(t1, av1, '--', label='a', color='black')

ax[1].set_xlabel('t')
ax[1].set_ylabel('v(t)')
ax[1].legend()
plt.tight_layout()
plt.savefig("E4_part1.svg",bbox_inches='tight') 
plt.show()

