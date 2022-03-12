import numpy as np


class ODESolver:
    """
    ODESolver Superclass
    ODE:
    u' = f(u, t), u(0) = U0

    """

    def __init__(self, f):
        self.f = f
        # f is right hand side of u' ie f(u, t)

    def set_initial_conditions(self, U0):
        '''
        U0 is initial condition
        U0 can be one value for scalar ODE (one equation)
        or an array for a system of equation (multiple equations)
        '''
        if isinstance(U0, (int, float)):
            # Scalar ODE
            self.number_of_eqs = 1
            U0 = float(U0)
        else:
            # System of ODEs
            U0 = np.asarray(U0)
            self.number_of_eqs = U0.size

        self.U0 = U0

    def solve(self, time_points):
        '''
        sets up the environment and solves
        '''
        self.t = np.asarray(time_points)
        n = self.t.size

        self.u = np.zeros((n, self.number_of_eqs))

        self.u[0, :] = self.U0

        # Numerical Integration
        '''
        advance() method contains algorithms to solve an equation
        by a specific numerical method (such as Forward Euler, Runge Kutta)
        advance() for a numerical methods is defined in respective subclass
        '''
        for i in range(n-1):
            self.i = i
            self.u[i+1] = self.advance()

        return self.u, self.t


'''
Numerical methods to solve ODEs are defined in following section

Currently there is only one method implemented in this project
I am thinking to continue working on it and add a few more schemes
'''


class ForwardEuler(ODESolver):
    """
    Subclass ForwardEuler of superclass ODESolver
    Solves ODE by Forward Euler numerical scheme
    Inherits superclass attributes
    """

    def advance(self):
        '''
        Provides solving mechanism
        '''
        u = self.u
        f = self.f
        i = self.i
        t = self.t

        dt = t[i+1] - t[i]

        return u[i, :] + dt * f(u[i, :], t[i])


if __name__ == "__main__":

    def f(u, t):
        return np.cos(t)

    T = 3
    dt = 0.5
    n = int(round(T//dt))
    time_points = np.linspace(0, T, n+1)

    solver = ForwardEuler(f)
    solver.set_initial_conditions(1)
    u, t = solver.solve(time_points)
    print(u, t)
