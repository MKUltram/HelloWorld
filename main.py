# Brandon Nelson
# 01/23/24
# Heads or Tails Probability
import random


# Function to create a random number that is either Heads or Tails
def coinflip():
    heads=0
    for i in range(100):
        if random.random() <= 0.5: # determines if it is Heads
            heads +=1
            return heads/100


def simulate(n):
    trails = []
    for i in range(n):
        trails.append(coinflip())
        print(sum(trails)/n)

simulate(1)
simulate(10)
simulate(100)

