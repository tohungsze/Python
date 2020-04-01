""" print the bottom line of Pascal's triangle
n=1                    1
n=2                1       1
n=3            1       2       1
n=4        1       3       3       1
n=5    1       4       6       4       1
"""


def pascal_triangle(n):
    li = []     # holder list
    if n == 1:
        return [1]
    else:
        li = pascal_triangle(n-1)
        # array.insert(index, value)
        # Insert an item at a given position. The first argument is the index of the element before
        # which to insert, so array.insert(0, x) inserts at the front of the list
        li.insert(0, 1)
        for i in range(1, len(li)-1):
            li[i] = pascal_triangle(n-1)[i-1] + pascal_triangle(n-1)[i]
        return li


print(pascal_triangle(6))

# codes from https://www.python-course.eu/recursive_functions.php
def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    return line

print(pascal(6))