import numpy as np
import matplotlib.pyplot as plt

tmax = 10 * np.pi  
h_values = [0.05, 0.01, 0.001, 0.0005]  

def exact_solution(t):
    return np.sin(t), np.cos(t)


def euler_method(h, tmax):
    N = int(tmax / h)
    t = np.linspace(0, tmax, N+1)
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    
    x[0] = 0  
    y[0] = 1 
    
    for i in range(N):
        x[i+1] = x[i] + h * y[i]  
        y[i+1] = y[i] - h * x[i] 
        
    return t, x, y


fig, ax = plt.subplots(1, 2, figsize=(12, 6))


for h in h_values:
    t, x_numerical, y_numerical = euler_method(h, tmax)
    x_exact, _ = exact_solution(t)

    ax[0].plot(t, x_numerical,'.', label=f'Numerical h={h}')
ax[0].plot(t, x_exact, linestyle='--', color='black', label='Exact Solution')

ax[0].set_xlabel('Time (t)')
ax[0].set_ylabel('x(t)')
ax[0].legend()


plt.figure(figsize=(12, 6))
for h in h_values:
    t, x_numerical, _ = euler_method(h, tmax)
    x_exact, _ = exact_solution(t)

    difference = x_numerical - x_exact
    ax[1].plot(t, difference,".", markersize = 3, label=f'Difference h={h}')


ax[1].set_xlabel('Time (t)')
ax[1].set_ylabel('Difference')
ax[1].legend()
plt.tight_layout()
plt.savefig("E3_graphs.svg",bbox_inches='tight')
plt.show()
