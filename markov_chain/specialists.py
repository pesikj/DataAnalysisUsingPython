import numpy as np
from numpy.linalg import inv
from scipy.stats import binom

#a1 = failed
#a2 = passed

testPassingProbabilities = [0.7, 0.6, 0.8, 0.9]
noOfSpecialistsCurrent = [100, 70, 50, 60]

wantedSpecialists = 5
wantedWithProbability = 0.9

transitionMatrix = np.zeros((len(testPassingProbabilities) + 2, len(testPassingProbabilities) + 2))
transitionMatrix[0, 0] = 1
transitionMatrix[1, 1] = 1

for i in range(2, len(testPassingProbabilities) + 1):
    listIndex = i - 2
    transitionMatrix[i, 0] = 1 - testPassingProbabilities[listIndex]
    transitionMatrix[i, i+1] = testPassingProbabilities[listIndex]
transitionMatrix[i+1, 0] = 1 - testPassingProbabilities[-1]
transitionMatrix[i+1, 1] = testPassingProbabilities[-1]

Q = transitionMatrix[2:,2:]
I = np.identity(len(testPassingProbabilities))
N = inv(I - Q)
R = transitionMatrix[2:,:2]
B = np.dot(N,R)

passVector = B[:, 1]
noOfSpecialistsFinal = round(sum(passVector * noOfSpecialistsCurrent), 3)
print(f"The expected number of specialists is {noOfSpecialistsFinal}.")
newStudentPassingProbability = float(passVector[0])

for employeesSentToCourse in range(wantedSpecialists, 100):
    probability = 1 - binom.cdf(wantedSpecialists - 1, employeesSentToCourse, newStudentPassingProbability)
    if probability > wantedWithProbability:
        print(f"{employeesSentToCourse} must be sent to the course.")
        break