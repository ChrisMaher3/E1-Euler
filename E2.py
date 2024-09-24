import numpy as np
import matplotlib.pyplot as plt

h = 0.05 #step size
tmax = 900

t0 = 0
x0 = 1
x1 = 3
x2 = 0
x3 = -0.7
x4 = -0.75


T = []
X = []
X1 = []
X2 = []
X3 = []
X4 = []

T.append(t0)
X.append(x0)
X1.append(x1)
X2.append(x2)
X3.append(x3)
X4.append(x4)


while T[-1] <= tmax:
    x5 = X[-1]+h*(T[-1]-(X[-1])**2)
    X.append(x5)
    x6 = X1[-1]+h*(T[-1]-(X1[-1])**2)
    X1.append(x6)
    x7 = X2[-1]+h*(T[-1]-(X2[-1])**2)
    X2.append(x7)
    x8 = X3[-1]+h*(T[-1]-(X3[-1])**2)
    X3.append(x8)
    #x9 = X4[-1]+h*(T[-1]-(X4[-1])**2)
    #X4.append(x9)
    t1 = T[-1] + h
    T.append(t1)

#plt.plot(np.sqrt(T),X, "k.", markersize = 3, )
plt.plot(T,X, "k.", markersize = 3, label = "X0 = 1")
#plt.plot(T,X1, "c.", markersize = 3, label = "X0 = 3")
#plt.plot(T,X2, "C1.", markersize = 3, label = "X0 = 0")
#plt.plot(T,X3, "C3.", markersize = 3, label = "X0 = -0.7")
#plt.plot(T,X4, "C2.", markersize = 3, label = "X0 = -0.75")
plt.xlabel("T")
plt.ylabel("X")
plt.legend()
plt.savefig("X0_1_t_X_tmax_900_stepsize_0.05.svg",bbox_inches='tight') 
plt.show()

