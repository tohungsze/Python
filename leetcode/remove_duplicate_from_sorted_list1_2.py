"""
1. Given a sorted linked list, delete all duplicates such that each element appear only once.
2. Given a sorted linked list, delete all nodes that have duplicate numbers,
   leaving only distinct numbers from the original list."""

import logging

logging.basicConfig(level=logging.INFO)


def remove_dup1(l1):
    if len(l1) <= 1:
        print("not long enough to have duplicate")
    result = [l1[0]]
    for i in range(1, len(l1)):
        if l1[i] != result[-1]:
            result.append(l1[i])

    print(result)

def remove_dup2(l2):
    if len(l2) <= 1:
        print("not long enough to have duplicate")
        print(l2)
    result2 = [l2[0]]
    for i in range(1, len(l2)):
        logging.debug(f" {i}, {l2[i]}, {result2}")
        if len(result2) == 0:
            result2.append(l2[i])
        elif l2[i] != result2[-1]:
            result2.append(l2[i])
        else:
            result2.pop()

    print(result2)


remove_dup1([1, 1, 2])  # [1, 2]
remove_dup1([1, 1, 2, 3, 3])    #[1, 2, 3]
remove_dup2([1, 2, 3, 3, 4, 4, 5])  # [1, 2, 5]
remove_dup2([1, 1, 2, 3])   # [2, 3]
