""" print factorial of a positive number n recursively """

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


# test
print("factorial of n = 10 is:", recursive_factorial(10))   # 362,880