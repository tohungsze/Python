"""Given a collection of distinct integers, return all possible permutations.
Two methods.
One does it manually. One uses itertools
Note:
will eat up memory if input is long
"""


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):    # for every char in the input string
            for i in range(len(elements)):      # build permutation putting first char all slots in rest of string
                # nb elements[0:1] works in both string and list contexts
                yield  perm[0:i] + elements[0:1] + perm[i:]


# test
result = []
for i in (all_perms([1, 2, 3, 4])):     # [[1, 2], [2, 1]]
    result.append(i)
print(result)
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# permutation([1,2,3])

# alternate solution based on itertool
import itertools as it


def permutations(iterable, r=None):
    pool = tuple(iterable)      # yield tuple instead of list to contrast the list from above
    n = len(pool)               # can change to tuple if needed
    r = n if r is None else r
    for indices in it.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[j] for j in indices)


result = []
for i in permutations([1, 2, 3, 4]):
    result.append(i)
print(result)
