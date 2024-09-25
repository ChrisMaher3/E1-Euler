import numpy as np
import matplotlib.pyplot as plt

# Define the time range and parameters
tmax = 10 * np.pi  # Cover at least 5 cycles of the sine wave
h_values = [0.05, 0.01, 0.001, 0.0005]  # Different time steps

# Define the exact solution
def exact_solution(t):
    return np.sin(t), np.cos(t)  # x = sin(t), y = cos(t)

# Function to perform Euler's method
def euler_method(h, tmax):
    N = int(tmax / h)
    t = np.linspace(0, tmax, N+1)
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    
    # Initial conditions
    x[0] = 0  # x(0) = 0
    y[0] = 1  # y(0) = 1
    
    for i in range(N):
        x[i+1] = x[i] + h * y[i]  # dx/dt = y
        y[i+1] = y[i] - h * x[i]  # dy/dt = -x
        
    return t, x, y

# Plotting the results
fi, ax = plt.subplots(1, 2, figsize=(12, 6))

# Loop over different time steps
for h in h_values:
    t, x_numerical, y_numerical = euler_method(h, tmax)
    x_exact, _ = exact_solution(t)

    # Plotting the numerical and exact solution
    ax[0].plot(t, x_numerical,'.', label=f'Numerical h={h}')
ax[0].plot(t, x_exact, linestyle='--', color='black', label='Exact Solution')

ax[0].set_xlabel('Time (t)')
ax[0].set_ylabel('x(t)')
ax[0].legend()
#.savefig("Different_timestamps_and_Exact.svg",bbox_inches='tight') 

# Calculate the differences and plot
plt.figure(figsize=(12, 6))
for h in h_values:
    t, x_numerical, _ = euler_method(h, tmax)
    x_exact, _ = exact_solution(t)
    
    # Calculate the difference
    difference = x_numerical - x_exact
    ax[1].plot(t, difference,".", markersize = 3, label=f'Difference h={h}')


ax[1].set_xlabel('Time (t)')
ax[1].set_ylabel('Difference')
ax[1].legend()
plt.tight_layout()
plt.savefig("Difference_at_various_timestep.svg",bbox_inches='tight') 
plt.show()
