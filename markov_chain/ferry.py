from quantecon import MarkovChain
import numpy as np

arrivalProbabilities = [0.2, 0.4, 0.2, 0.1, 0.06, 0.04]
numberOfPlaces = 4

transitionMatrix = np.zeros((numberOfPlaces + 1, numberOfPlaces + 1))

for row in range(0, numberOfPlaces + 1):
    if row in (0, 1):
        startColumn = 0
    else:
        startColumn = row - 1
    probabilityIndex = 0
    for column in range(startColumn, numberOfPlaces + 1):
        if column < numberOfPlaces:
            transitionMatrix[row, column] = arrivalProbabilities[probabilityIndex]
        else:
            transitionMatrix[row, column] = sum(arrivalProbabilities[probabilityIndex:])
        probabilityIndex += 1

print(transitionMatrix)

mc = MarkovChain(transitionMatrix)
numberOfCars = np.array(np.linspace(0, numberOfPlaces, num=numberOfPlaces+1, dtype=np.dtype(np.int16)))
stationaryVector = np.array(mc.stationary_distributions[0,:])
print(stationaryVector)
print(sum(numberOfCars * stationaryVector))