""" implementing merge sort
pseudo codes:
split the input list into half, left and right
merge sort left, merge sort right
merge the two halves
average: nlog(n)
worse case: nlog(n)
"""


import traceback
import random
import time


def merge(li, left, right):
    i = 0   # index for left
    j = 0   # index for right
    k = 0   # index for result list

    while i < len(left) and j < len(right): # and k < len(left) + len(right)):
        if left[i] < right[j]:
            li[k] = left[i]
            i += 1
        else:
            li[k] = right[j]
            j += 1
        k += 1

    # the following copy remaining of one of the list as either one of them gets to end first in line 16
    # eg if you start with left with 2 elements all smaller than those in right (with 3 elements)
    # when all of left would have been put in original list but none of the right isn't there
    # hence need to copy the 3 elements from right side
    while i < len(left):
        li[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        li[k] = right[j]
        j += 1
        k += 1


def merge_sort(li):

    if len(li) > 1:

        mid = int(len(li)/2)
        left = li[:mid]
        right = li[mid:]

        #print(left, right)
        result = []
        merge_sort(left)
        merge_sort(right)
        merge(li, left, right)


li = [5, 7, 2, 9, 3, 1, 4, 6, 8]    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
li1 = [1, 2, 3, 4, 9, 8, 7, 6]  # [1, 2, 3, 4, 6, 7, 8, 9]

# test
merge_sort(li)
print(li)
merge_sort(li1)
print(li1)

li2 = []
merge_sort(li2)
print(li2)

li3 = [5]
merge_sort(li3)
print(li3)

try:
    merge_sort("dadsd")
except:
    print("Something went wrong")

# time taken
x = 1_000_000
li4 = []
for i in range(x):
    li4.append(random.randint(0, x))
start_time = time.time()
merge_sort(li4)
end_time = time.time()
print(f"time taken to merge sort list of ", len(li4), ":")
print("{:.2f}".format(end_time - start_time), "sec")


def sort_quick_pivot(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = sort_quick_pivot(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = sort_quick_pivot(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


x = 1_000_000
li5 = []
for i in range(x):
    li5.append(random.randint(0, x))
start_time = time.time()
sort_quick_pivot(li5)
end_time = time.time()
print(f"time taken to quick sort list of ", len(li4), ":")
print("{:.2f}".format(end_time - start_time), "sec")

