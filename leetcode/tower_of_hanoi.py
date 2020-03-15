""" Tower of Hanoi
Move all disc from A to C with B empty when starting.
Disc can only be put on top of another disc smaller than in"""
steps = 0


def move(a, b):  # move from a to b
    global steps
    print("move from %s to %s" % (a, b))
    steps += 1


def move_via(a, b, c):  # move from a to c via b
    move(a, b)
    move(b, c)


# test
# move_via("a", "b", "c")

def tower_of_hanoi(n, a, b, c):
    global steps  # step is number of moves taken
    if n == 0:
        pass  # when we get to n == 0, we are done
    else:
        tower_of_hanoi(n - 1, a, c, b)  #
        move(a, c)
        tower_of_hanoi(n - 1, b, c, a)  # end of function


tower_of_hanoi(4, "A", "B", "C")
print("total number of steps:", steps)
