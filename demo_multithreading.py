# Execution time calculation for a multi-threaded Python program

import time
from threading import Thread

def calculateSum(n):
    sum = 0
    for i in range(n):
        sum += i

n = 100000000
T1 = Thread(target=calculateSum, args=(n//2,))
T2 = Thread(target=calculateSum, args=(n//2,))
startTime = time.time()
T1.start()
T2.start()
T1.join()
T2.join()
endTime = time.time()

print("Time taken in multi-thread = ", endTime - startTime)

# Time taken in multi-thread =  2.601400136947632 seconds
