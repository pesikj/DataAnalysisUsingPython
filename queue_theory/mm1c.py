import numpy as np
λ = 28/8
μ = 4
k = 5

ρ = λ / μ
ρExpN = np.zeros(k + 1)
for i in range(k+1):
    ρExpN[i] = ρ ** i
p_0 = 1 / sum(ρExpN)
p_n = np.zeros(k + 1)
for i in range(k+1):
    p_n[i] = p_0 * ρExpN[i]

n = np.array(np.linspace(0, k, num=k+1, dtype=np.dtype(np.int16)))
EN_s = sum(n * p_n)
nInQueue = np.array(np.linspace(0, k-1, num=k, dtype=np.dtype(np.int16)))
EN_f = sum(nInQueue * p_n[1:])
λstar = λ * (1 - p_n[-1])

print(f"p_0 = {round(p_0, 4)}")
print(f"p_{k} = {round(p_n[-1], 4)}")
print(f"λstar = {round(λstar, 4)}")
print(f"E(N_s) = {round(EN_s, 4)}")
print(f"E(N_f) = {round(EN_f, 4)}")
print(f"E(T_s) = {round(EN_s/λstar, 4)}")
print(f"E(T_f) = {round(EN_f/λstar, 4)}")