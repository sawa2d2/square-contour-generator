import numpy as np
import math

class benchmarks:

    def sample(self, X, Y):
        return Y * np.cos(X)

    # for swarm intelligence
    def sphere(self, X, Y):
        return X**2 + Y**2

    def rosenbrock(self, X, Y):
        return (1 - X)**2 + 100 * (Y - X**2)**2
    
    def rastrigin(self, X, Y):
        return X**2 + Y**2 + 10 * (2 - np.cos(2 * math.pi * X) - np.cos(2 * math.pi * Y))

    def ackley(self, X, Y):
        term1 = np.exp(-0.2 * np.sqrt(0.5 * (X**2 + Y**2)))
        term2 = np.exp(0.5 * (np.cos(2 * math.pi * X) + np.cos(2 * math.pi * Y)))
        return 20 - 20 * term1 + math.e - term2

    def griewank(self, X, Y):
        term1 = (X**2 + Y**2) / 4000
        term2 = np.cos(X) * np.cos(Y / math.sqrt(2))
        return term1 - term2 + 1
    
    ## for coverage control
    def gauss(self, X, Y):
        return np.exp(-20 * np.sqrt((X - 0.8)**2 + (Y - 0.6)**2))
