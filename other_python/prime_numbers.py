# tries to compare time difference when calculating prime numbers in 1-1000
# first method is brute force (somewhat optimized)
# second method tries to eliminate all numbers which are multiple of previously
#     calculated numbers (Sieve of Eratosthenes)
# strangely, Sieve of Eratosthenes is slower than the first method
import time
import math


# brute force
def time1(x):
    prime_list = [1, 2]
    for num in range(3, x+1, 2):
        is_prime = True
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            prime_list.append(num)
    #print(prime_list)


# build a list of all numbers
# eliminate any number divisible by each already calculated prime
def time2(x):
    start_list = []  # this is the list holding all numbers at beginning
    for i in range(1, x + 1):
        start_list.append(i) # extremely slow
    y = 2
    while y * y < x:
        for z in range(y * y, x + 1, y):
            if z in start_list:
                start_list.remove(z)
        y += 1
    print(start_list)

# same as method 2 but without append, use an input list instead
def time3(start_list):
    y = 2
    for x in start_list:
        while y * y < x:
            for z in range(y * y, len(start_list) + 1, y):
                if z in start_list:
                    start_list.remove(z)
            y += 1
    print(start_list)

#n = 100_000  # n is the range for numbers to find prime

#print("Prime numbers in 1 to", "{:,}".format(n))
#not finished
ratios = []

m=2
for turn in range(m):
    rounds = [10_00, 10_000, 100_000]
    #ratios = []
    ratio1, ratio2, ratio3 = {}, {}, {}
    for round in rounds:
        startt1 = time.time()
        time1(round)
        endt1 = time.time()
        elapsed_1 = endt1 - startt1
        #print("elapsed time for method1:", "{:.3f}".format(elapsed), "seconds")

        startt2 = time.time()
        time2(round)
        endt2 = time.time()
        elapsed_2 = endt2 - startt2

        start_list = []  # this is the list holding all numbers at beginning
        for i in range(1, round + 1):
            start_list.append(i)

        startt3 = time.time()
        time3(start_list)
        endt3 = time.time()
        elapsed_3 = endt3 - startt3
        #print("elapsed time for method2:", "{:.3f}".format(elapsed), "seconds")

        #print("round", round, "ratio =", elapsed_1/elapsed_2)
        #ratios[round]=elapsed_1/elapsed_2

        #time_taken1.append(elapsed_1)
        #time_taken2.append(elapsed_2)
        ratios.append(elapsed_1 / elapsed_2)
        print("elapsed time for method1:", "{:.3f}".format(elapsed_1), "seconds")
        print("elapsed time for method2:", "{:.3f}".format(elapsed_2), "seconds")
        print("elapsed time for method3:", "{:.3f}".format(elapsed_3), "seconds")
        if elapsed_3 != 0:
            print("for primes in", round, "ratio between brute force and Seieve of Erasothene:",
                  "{:.3f}".format(elapsed_1 / elapsed_3))