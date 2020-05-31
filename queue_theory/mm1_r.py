import numpy as np
import math
λ = 2
μ = 25
r = 8

x = np.zeros(r + 1)
for i in range(r+1):
    x[i] = (λ / μ) ** i * math.factorial(r) / math.factorial(r - i)
p_0 = 1 / sum(x)
p_n = np.zeros(r + 1)
for i in range(r+1):
    p_n[i] = p_0 * x[i]

n = np.array(np.linspace(0, r, num=r+1, dtype=np.dtype(np.int16)))
EN_s = sum(n * p_n)
nInQueue = np.array(np.linspace(0, r-1, num=r, dtype=np.dtype(np.int16)))
EN_f = sum(nInQueue * p_n[1:])
λstar = λ * (r - EN_s)

print(f"p_0 = {round(p_0, 4)}")
print(f"1 - p_0 = {round(1 - p_0, 4)}")
print(f"λstar = {round(λstar, 4)}")
print(f"E(N_s) = {round(EN_s, 4)}")
print(f"E(N_f) = {round(EN_f, 4)}")
print(f"E(T_s) = {round(EN_s/λstar, 4)}")
print(f"E(T_f) = {round(EN_f/λstar, 4)}")
