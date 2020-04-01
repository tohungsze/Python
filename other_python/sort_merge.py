""" implementing merge sort
pseudo codes:
split the input list into half, left and right
merge sort left, merge sort right
merge the two halves
"""


import traceback
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

