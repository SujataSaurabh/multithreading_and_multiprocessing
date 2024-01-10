import time
from multiprocessing import Process

def calculateSum(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
    return sum

def main():
    n = 100000000
    start_time = time.time()

    # Split the range into two halves
    mid = n // 2

    # Create two separate processes
    P1 = Process(target=calculateSum, args=(0, mid))
    P2 = Process(target=calculateSum, args=(mid, n))

    # Start the processes
    P1.start()
    P2.start()

    # Wait for both processes to finish
    P1.join()
    P2.join()

    # Get the results from the processes
    sum_result = P1.exitcode + P2.exitcode

    end_time = time.time()

    print("Sum =", sum_result)
    print("Time taken in multiprocessing = ", end_time - start_time)

if __name__ == "__main__":
    main()

# Time taken in multiprocessing =  1.4500269889831543 seconds 
