import numpy as np
from ODElib.ODESolver import ODESolver, ForwardEuler
from matplotlib import pyplot as plt


def f(u, t):
    '''
    Input function 'f' for ODESolver
    User can modify return value to solve form an equation

    Try using familiar functions like exponent of t ie np.exp(t)
    or cosine(t) ie np.cos(t) to verify the solution by graph
    '''
    return -np.cos(t)


# Time
T = 10

# Time Step Size
dt = 0.1

# Number of time steps
n = int(round(T/dt))

# Setup initial array
time_points = np.linspace(0, T, n+1)

# Solve
solver = ForwardEuler(f)
solver.set_initial_conditions(1)
u, t = solver.solve(time_points)
print(
    f"Following are the values of function at each time step\n {u} \n")
print(f"Change is time steps\n: {t}")


'''  Graph of the rate of change of given function '''

plt.plot(t, u, label='Function')
plt.xlabel('Time')
plt.ylabel('Function')
plt.legend()
plt.show()
