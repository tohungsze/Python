"""The atoi() function takes a string (which represents an integer) as an argument and returns its value."""

def a_to_i(s):
    if len(s) == 1:
        return int(s[0])
    else:
        return int(a_to_i(s[0:len(s)-1]))*10 + int(s[-1])


# test
print(a_to_i("1") + 1)      # a_to_i("1") = 1, result = 1 + 1 => 2
print(a_to_i("12") + 1)     # a_to_i("1") = 1, result = 12 + 1 => 13
print(a_to_i("123") + 1)    # a_to_i("1") = 1, result = 123 + 1 => 124
print(a_to_i("1234") + 1)   # a_to_i("1") = 1, result = 1234 + 1 => 1235