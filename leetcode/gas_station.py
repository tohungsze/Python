"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
"""

def gas_station(gas, cost):

    # helper function to test just one starting point
    def calculate_loop(i):
        tank = 0
        current = i
        end = i

        for j in range(len(gas)):
            tank = tank + gas[current] - cost[current]
            if tank >= 0:       # enough gas to get to next stop
                if current + 1 == end:
                    return True
                elif current + 1 == len(gas):
                    current = 0
                else:
                    current += 1
            else:
                return False


    # start of main function
    # fail quick - if total gas < total cost, definitely can't make a loop no mater where you start
    if sum(gas) < sum(cost):
        return "not able to find starting , fail quick"

    # there must be a valid starting point
    for i in range(len(gas)):
        # calculate each loop with i as starting point
            if calculate_loop(i):
                return i
    else:
        return "not able to find starting point"


# test
gas1  = [1,2,3,4,5]  # output 3
cost1 = [3,4,5,1,2]
print("test1:", gas_station(gas1, cost1))

gas2  = [2,3,4]     # not able to make a loop
cost2 = [3,4,3]
print("test2:", gas_station(gas2, cost2))
