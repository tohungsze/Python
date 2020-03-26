"""Given an input string, reverse the string word by word."""


def reverse_builtin(l):
    x = ""
    for i in reversed([word for word in l.split()]):
        x = x + " " + i
    print(x.strip())


def reverse_no_func(l):
    x = ""
    words = []
    temp = ""
    for i in range(len(l)):
        if l[i] != " ":
            temp = temp + l[i]
        elif temp != "":
            words.append(temp)
            temp = ""
        if i == len(l) - 1 and temp != "":
            words.append(temp)

    answer = ""
    for i in range(-1, -(1+len(words)), -1):
        answer += words[i]
        if i != -1 - len(words):
            answer += " "
    print(answer)


# test
l1 = "the sky is blue"      # "blue is sky the"
l2 = "  hello world!  "     # "world! hello", Your reversed string should not contain leading or trailing spaces.
reverse_builtin(l1)
reverse_builtin(l2)

reverse_no_func(l1)
reverse_no_func(l2)