import numpy as np
import matplotlib.pyplot as plt

# Model parameters
N = 1000000 # Total population
beta = 0.2  # Infection rate 
p = 0.7 # Proportion asymptomatic
sigma_a = 0.5 # Rate asymptomatic infectious
sigma_s = 0.5 # Rate symptomatic infectious  
phi = 0.1 # Hospitalization rate
gamma_h = 0.9 # Recovery rate (hospitalized)
mu_nh = 0.1 # Mortality rate (non-hospitalized)  
alpha = 0.8 # Recovery rate (asymptomatic)

# Initial conditions
S0 = 999900
Ea0 = 50 
Es0 = 50
I0 = 0
H0 = 0
NH0 = 0
R0 = 0
D0 = 0

# Time steps
t_max = 365
dt = 1
t = np.arange(0, t_max, dt)

# Lists to store values
S, Ea, Es, I, H, NH, R, D = [],[],[],[],[],[],[],[]

# Initial conditions
S.append(S0)
Ea.append(Ea0)
Es.append(Es0)  
I.append(I0)
H.append(H0)
NH.append(NH0)
R.append(R0)
D.append(D0)

for i in range(len(t)-1):
    
    S_i = S[i]
    Ea_i = Ea[i]  
    Es_i = Es[i]
    I_i = I[i]
    H_i = H[i]
    NH_i = NH[i]
    R_i = R[i]
    D_i = D[i]

    dSdt = -beta*S_i*(I_i + Ea_i + Es_i)/N  
    dEadt = p*beta*S_i*(I_i + Ea_i + Es_i)/N - sigma_a*Ea_i - alpha*Ea_i
    dEsdt = (1-p)*beta*S_i*(I_i + Ea_i + Es_i)/N - sigma_s*Es_i
    dIdt = sigma_a*Ea_i + sigma_s*Es_i - phi*I_i - (1-phi)*I_i
    dHdt = phi*I_i - gamma_h*H_i - (1-gamma_h)*H_i
    dNHdt = (1-phi)*I_i - mu_nh*NH_i - (1-mu_nh)*NH_i 
    dRdt = gamma_h*H_i + (1-mu_nh)*NH_i + alpha*Ea_i
    dDdt = (1-gamma_h)*H_i + mu_nh*NH_i

    S.append(S_i + dSdt*dt)
    Ea.append(Ea_i + dEadt*dt)
    Es.append(Es_i + dEsdt*dt)
    I.append(I_i + dIdt*dt)
    H.append(H_i + dHdt*dt)
    NH.append(NH_i + dNHdt*dt)
    R.append(R_i + dRdt*dt)
    D.append(D_i + dDdt*dt)

# Plot    
plt.plot(t, S, label='Susceptible')
plt.plot(t, Ea, label='Exposed asymptomatic')
plt.plot(t, Es, label='Exposed symptomatic') 
plt.plot(t, I, label='Infected')
plt.plot(t, H, label='Hospitalized')
plt.plot(t, NH, label='Not hospitalized')
plt.plot(t, R, label='Recovered')
plt.plot(t, D, label='Deaths')

plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.legend()
plt.show()
