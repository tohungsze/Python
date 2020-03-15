''' Implement pow(x, n), which calculates x raised to the power n. '''

# print("FORMAT".format(NUMBER))

def pow(i, n):
    n = int(n)          # making sure we only deal with n as integer
    # if not str(i).isdigit() or not str(n).isdigit():
    #     print("wrong input")
    #     quit()
    if n == 0:
        return 1
    elif n < 0:
        return float(1 / pow(i, -1 * n))
    elif i == 0 and n > 0:
        return 0
    elif i > 1 and n > 0:
        return i * pow(i, n-1)


#test print("FORMAT".format(NUMBER))
print("{:.5f}".format(pow(2.00000, 10)))         # 1024.00000
print("{:.5f}".format(pow(2.10000, 3)) )         # 9.26100
print("{:.5f}".format(pow(2.00000, -2)))          # 0.25000
