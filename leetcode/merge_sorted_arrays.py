"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

My Note:
First move all of nums1 (that have been initialized) to end of nums1 maintaining the order.
Then one by one, compare and move nums1, nums2 into position

"""
def merge(nums1, m, nums2, n):
    print("BEFORE merge, the lists are {}, {}".format(nums1, nums2))
    pos1 = 0   # these are the current position of the element in each list to be copied next
    pos2 = 0

    # move everything from nums1 to end to make room
    for i in range(m):
        nums1[-1 - i] = nums1[len(nums1) - 1 - m - i]    # lens(nums1) - 1 is the end index of the last element
        nums1[len(nums1) - 1 - m - i] = 0
    pos1 = len(nums1) - m
    # now, all elements in nums1 moved to the end, first m elements are set to 0

    i = 0
    while(True):
        if nums1[pos1] < nums2[pos2]:
            nums1[i] = nums1[pos1]
            pos1 += 1
            i += 1

            if pos1 >= len(nums1):  # nums1 is done, need to copy rest of nums2
                pos1 = m + n - len(nums2[pos2:])
                for j in range(len(nums2[pos2:])):  # copy rest of nums2 to num1
                    nums1[pos1] = nums2[pos2]
                    pos1 += 1
                    pos2 += 1
                break
        else:
            nums1[i] = nums2[pos2]
            pos2 += 1
            if pos2 >= len(nums2):   # num2 is done
                # copy rest of nums1
                pos1 = m + n - len(nums1[pos1:])
                for j in range(len(nums1[pos1:])):
                    nums1[pos1] = nums1[pos1]
                    pos1 += 1
                    pos2 += 1
                break
            else:
                i += 1
    print("AFTER merge, the lists are {}, {}".format(nums1, nums2))



# test
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)   #[1,2,2,3,5,6]

nums3 = [1, 2, 6, 0, 0, 0]
m = 3
nums4 = [2, 5, 6]
n = 3
merge(nums3, m, nums4, n)   #[1,2,2,5,6,6]




# test
