""" function to check if an input string is camel case:
start with lower case and every word after begins with c1 apital letter
https://google.github.io/styleguide/javaguide.html#s5.3-camel-case """


import re

def is_camel_case(s):
    """

    :type s: str
    """
    special_char = re.compile('[_@_!#$%^&*()<>?/\|}{~:]')
    upper = re.compile('[A-Z]')
    index = []  # list to contain indexes of all upper case chars
    words = []  # list of each individual word

    # check that input is a string
    if type(s) != str:
        return False

    # check that input is a non-zero length string
    elif s == "":  # has to have at least 2 chars
        return False

    # check that there is no special char like "'"
    elif special_char.search(s) is not None:
        return False

    # check if first char is lower case
    elif s.istitle():
        return False

    # check if it has at least 1 upper case
    elif s == s.lower():
        return False

    # check that the last char is not upper case
    if upper.match(s[-1]):
        return False

    # find index of the upper case chars, put in a list
    for i in range(len(s)):
        if upper.match(s[i]):
            index.append(i)
    if len(index) == 0:
        return False

    # check that upper case char is not followed by another upper case
    for i in index:
        if i + 1 in index:
            return False
    else:
        # print all words
        temp = 0
        for i in index:
            words.append(s[temp:i])
            temp = i
        words.append(s[temp:])
        print("s is in camel case, each word are", words)
        return True


# test
print(3, is_camel_case(int(3)))   # False, input is not a string
print(" (empty string)", is_camel_case(""))  # False, input is a non-zero length string
print("a", is_camel_case("a"))   # False, not at least 2 chars
print(r"a/b", is_camel_case(r"a/b"))    # False, no special char like "'"
print(r"a_b", is_camel_case(r"a_b"))    # False, no special char like "_"
print("Abc", is_camel_case("Abc"))  # False, first char is not lower case
print("abcd", is_camel_case("abcd"))    # False, no upper case
print("abA", is_camel_case("abA"))    # False, last char is upper case
print("abcDE", is_camel_case("abcDEf"))  # upper case char is not followed by another upper case
print("abcDefGhiJkl", is_camel_case("abcDefGhiJkl"))    # True

print("from internet")
print("#1")  # https://stackoverflow.com/questions/10182664/check-for-camel-case-in-python
sub_string = "hiSantyWhereAreYou"  # Change the string here and try
index=[x for x,y in enumerate(list(sub_string)) if(y.isupper())]  # Finding the index of caps
camel_=[]
temp=0
for m in index:
    camel_.append(sub_string[temp:m])
    temp=m
if len(index) > 0:
    camel_.append(sub_string[index[-1]::])
    print('The individual camel case words are', camel_)  # Output is in list
else:
    camel_.append(sub_string)
    print('The given string is not camel Case')


print("#2, with inflection")
import inflection


def is_camel_case1(s):
    return inflection.camelize(s, uppercase_first_letter=False) == s


print("hiSantyWhereAreYou", is_camel_case1("hiSantyWhereAreYou"))
