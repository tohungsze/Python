# demonstrate fibonacci with and without caching

'''
# this is really slow, can't handle more than 30 ish numbers
def fibonacci_n(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci_n(n-1) + fibonacci_n(n-2)

for i in range(1, 11):
    print("fibonacci(", i, ") is:", fibonacci_n(i))
'''

'''
cache_dict = {}
# manual caching
def fibonacci_mc(n): # mc = manual cache
    global cache_dict
    if n in cache_dict:
        return cache_dict[n]

    if n == 1 or n == 2:
        #cache_dict[n]=1
        result = 1
    else:
        result = fibonacci_mc(n-1) + fibonacci_mc(n-2)

    cache_dict[n] = result
    return result

for i in range(1, 1001):
    print("fibonacci(", i, ") is:", fibonacci_mc(i))
'''

# using functools lru
# with lru, originally slow simple calculation is fast!
# each function will have own cache
from functools import lru_cache

@lru_cache(maxsize = 1000) #default is 128
def fibonacci_lru(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

for i in range(1, 10001):
    print("fibonacci(", i, ") is:", fibonacci_lru(i))