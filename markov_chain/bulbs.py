from quantecon import MarkovChain
import numpy as np

failureProbabilities = [0.2, 0.4, 0.3, 0.1]

transitionMatrix = np.zeros((len(failureProbabilities), len(failureProbabilities)))
currentDenominator = 1
for i in range(len(transitionMatrix)):
    transitionProbability = failureProbabilities[i] / currentDenominator
    transitionMatrix[i, 0] = transitionProbability
    if i < len(transitionMatrix) - 1:
        transitionMatrix[i, i + 1] = 1 - transitionProbability
    currentDenominator *= 1 - transitionProbability

print(transitionMatrix)

mc = MarkovChain(transitionMatrix)
age = np.array(np.linspace(0, len(failureProbabilities), num=len(failureProbabilities), dtype=np.dtype(np.int16)))
stationaryVector = np.array(mc.stationary_distributions[0,:])
print(stationaryVector)
print(sum(age * stationaryVector))