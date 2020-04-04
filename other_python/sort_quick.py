""" quick sort """
# find pivot point where everything smaller than it is on the left of it
# everything larger than it is on the right
# Put everything smaller than the pivot in a list
# Put everything larger than the pivot in another
# Put everything equal to the pivot in final list
# Run quick sort again on the smaller list and larger list until they are all sorted
# In a random input list, every element is as good an element to start as any other
# Randomizing position of pivot makes it more likely to avoid picking the worse case(?)
# best case: nlog(n)
# worst case: n**2 (input is an already sorted list)
# also included two functions - one manually tracking the pivot, one with built-in function
# built-in function in Python 3 is much, much faster than either of the manually created method
import random
import time


def sort_quick(a):
    if len(a) <= 1: return a
    smaller, equal, larger = [], [], []
    pivot = a[random.randint(0, len(a) - 1)]    # randint is a method in Python 3

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            larger.append(x)

    return sort_quick(smaller) + equal + sort_quick(larger)


# test
li = [3, 2, 1, 4]
li1 = [5, 7, 2, 9, 3, 1, 4, 6, 8]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = [1, 2, 3, 4]
li3 = [1, 10, 2, 2, 3, 4]
print(sort_quick(li))
print(sort_quick(li1))
print(sort_quick(li2))
print(sort_quick(li3))


# time taken
#x = 10_000_000
x = 100
li4 = []
li4a = []
li5 = []
li5a = []
li6 = []
for i in range(x):
    n = random.randint(0, x)
    li4.append(n)
    li5.append(n)
    li6.append(n)


# print(sort_quick(li4))
start_time = time.time()
li4a = sort_quick(li4)
end_time = time.time()
time_taken = end_time - start_time
print("li4 before sort:", li4)
print("li4a after sort", li4a)
print(f"time taken to quick sort list of", len(li4), "with method 1:", "{:.2f}".format(end_time - start_time), "sec")

# repeat on sorted list
start_time = time.time()
sort_quick(li4a)
end_time = time.time()
print(f"time taken to quick sort list of SORTED", len(li4), "with method 1:", "{:.2f}".format(end_time - start_time), "sec")
print()


# from internet
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


start_time = time.time()
li5a = sort_quick_pivot(li5)
end_time = time.time()
print("li5 before sort", li5)
print("li5a after sort", li5a)
print(f"time taken to quick sort list of", len(li4), "with method 2:", "{:.2f}".format(end_time - start_time), "sec")

# repeat on sorted list - can't run this on 20,000 already sorted list => too many partitions
# start_time = time.time()
# sort_quick_pivot(li5a)
# end_time = time.time()
# print(f"time taken to quick sort list of SORTED", len(li5), "with method 2:", "{:.2f}".format(end_time - start_time), "sec")
# print()

# using built-in
print("li6 before sort:", li6)
start_time = time.time()
li6.sort()
end_time = time.time()
print(f"time taken to quick sort list of", len(li6), "using BUILT-IN function:", "{:.2f}".format(end_time - start_time), "sec")
print("li6 after sort: ", li6)
start_time = time.time()
li6.sort()
end_time = time.time()
print(f"time taken to quick sort list of SORTED", len(li6), "using BUILT-IN function:", "{:.2f}".format(end_time - start_time), "sec")