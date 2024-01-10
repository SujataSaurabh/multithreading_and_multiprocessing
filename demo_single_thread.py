#Single threaded: 
# Execution time calculation for a single-threaded Python program

import time

def calculateSum(n):
    sum = 0
    for i in range(n):
        sum += i

n = 100000000
startTime = time.time()
calculateSum(n)
endTime = time.time()

print("Time taken in single thread = ", endTime - startTime)

# takes about 2.4596879482269287 seconds on my machine
