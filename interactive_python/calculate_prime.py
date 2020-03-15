"""
Convert the following English description into code.

Initialize n to be 1000. Initialize numbers to be a list of numbers from 2 to n but not including n.
With results starting as the empty list, repeat the following as long as numbers contains any numbers.
Add the first number in numbers to the end of results.
Remove every number in numbers that is evenly divisible by
(has no remainder when divided by) the number that you had just added to results.
How long is results?

To test your code, when n is instead 100, the length of results is 25.
"""

switch = True
number = 1000
results = []
numbers = []
tmp1 = []
tmp2 = []

for i in range(2, number):
    numbers.append(i)

n = 0

while (switch):
    n += 1

    # make tmp1 same as numbers
    for a in numbers:
        tmp1.append(a)

    print("round: " + str(n) + ", switch: " + str(switch))

    results.append(numbers[0])

    # main operation
    for m in tmp1:
        if m % numbers[0] == 0:
            tmp1.remove(m)

    # check switch
    if len(tmp1) == 0:
        switch = False

    # copy numbers from tmp1
    numbers = []
    for a in tmp1:
        numbers.append(a)
    # print numbers

    tmp1 = []
    tmp2 = []

print("results: " + str(results))
print("answer= " + str(len(results)))