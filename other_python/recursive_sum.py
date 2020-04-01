""" Given a positive integer, calculate the sum of all integers from 1 to n (including n), recursively """


def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)


# test
print("sum of 1 - 10 is:", recursive_sum(10))    # 55


def recursive_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recursive_list(l[1:])     # l[1:] is done by copying the elements in l[1:] and create a new list
                                                # slow


# test
print("sum of list [1, 2, 3] is:", recursive_list([1, 2, 3]))   # 6
