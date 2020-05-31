import random
cards = [1, 1, 2, 3, 4, 5, 6, 7, 7, 7]

nsim = 1000000
hit = 0

for i in range(nsim):
  sum = 0
  for j in range(100):
    index = random.randrange(len(cards))
    sum += cards[index]
  if 420 <= sum <= 460:
    hit += 1
print(hit/nsim)