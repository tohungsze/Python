# Given an unsorted integer array, find the smallest missing positive integer.
def first_missing_positive(l):
    i = min(l)
    # print("min(l)", i)
    done = True
    if i >= 0:
        # start from min and count 1 up until finding answer
        if 1 not in l:      # min is smaller than 0
            return 1
        else:
            while(done):
                if i + 1 not in l:
                    return i + 1
                else:
                    i += 1

    i = 0       # min(l) < 0
    # print("min(l) < 0")
    while (done):
        if i + 1 not in l:
            return i + 1
        else:
            i += 1

# test
print(first_missing_positive([1,2,0]))
#print(min([1,2,0]))
#Output: 3

print(first_missing_positive([3,4,-1,1]))
#Output: 2

print(first_missing_positive([7,8,9,11,12]))
#Output: 1
