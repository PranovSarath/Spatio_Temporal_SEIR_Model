import numpy as np
import matplotlib.pyplot as plt
import pyross

# Define parameters
beta = 0.2       # Transmission rate
sigma = 1/5      # Transition from exposed to infectious
gamma = 1/10     # Recovery rate

# Define initial conditions
N = 1000         # Total population
I0 = 1           # Initial number of infectious individuals
E0 = 0           # Initial number of exposed individuals
S0 = N - E0 - I0 # Initial number of susceptible individuals
R0 = 0           # Initial number of recovered individuals

# Define contact matrix (for a simple model, this can be an identity matrix)
contact_matrix = np.identity(4)

# Create a dictionary to configure the model
model_spec = {
    "classes": ["S", "E", "I", "R"],
    "S": S0,
    "E": E0,
    "I": I0,
    "R": R0,
    "parameters": {
        "beta": beta,
        "sigma": sigma,
        "gamma": gamma
    },
    "transitions": [
        {"from": "S", "to": "E", "rate": "beta*I"},
        {"from": "E", "to": "I", "rate": "sigma"},
        {"from": "I", "to": "R", "rate": "gamma"}
    ],
    "matrix": contact_matrix
}

# Create the model object
model = pyross.models.Spp(model_spec, t_start=0, t_end=100, dt=0.1)

# Simulate the model
result = model.simulate()

# Plot the results
plt.plot(result["t"], result["X"][:, 0], label="S")
plt.plot(result["t"], result["X"][:, 1], label="E")
plt.plot(result["t"], result["X"][:, 2], label="I")
plt.plot(result["t"], result["X"][:, 3], label="R")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()
