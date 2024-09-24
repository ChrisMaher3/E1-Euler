import numpy as np
import matplotlib.pyplot as plt

dt = 1
tmax = 10
tau = 2

t0 = 0
n0 = 10

T = []
N = []
Nr = []

T.append(t0)
N.append(n0)
Nr.append(n0)

while (T[-1]-tmax) < tau/2:
    n1 = (N[-1])-((N[-1]*dt)/tau)
    N.append(n1)
    t1 = T[-1] + dt
    T.append(t1)
    n2 = n0*np.exp(-(T[-1]/tau))
    Nr.append(n2)

Nar = np.array(N)
Nrar = np.array(Nr)

Nrara = np.subtract(Nrar, Nar)
Nc = list(Nrara)

plt.plot(T,Nc,"k.", label = "X1 = 0")
plt.plot(T,Nr, "C1.", label = "Exact Data")
#plt.plot(T,N, "k.", label = "Calculated Data")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Number of Nuclei")
#plt.savefig("Difference_1_timestep.svg",bbox_inches='tight') 
plt.show()

