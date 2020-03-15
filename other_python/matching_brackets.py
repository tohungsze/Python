# a function to check if input list of brackets
# matches left and right sides
# e.g. [{}] returns true
# [{]}, [[{}], }{}[] fails

# method using just one list
def match_brackets(s):
    holder = []
    set_left = ("(", "[", "{")
    for x in s:
        if x in set_left:
            holder += x
        else:
            if x == ")":
                if len(holder) == 0:
                    return False
                else:
                    y = holder.pop()   # pop() without parameter removes the last one
                    if y != "(":
                        return False

            if x == "]":
                if len(holder) == 0:
                        return False
                else:
                    y = holder.pop()  # pop() without parameter removes the last one
                    if y != "[":
                        return False

            if x == "}":
                if len(holder) == 0:
                    return False
                else:
                    y = holder.pop()  # pop() without parameter removes the last one
                    if y != "{":
                        return False

    if len(holder) == 0:
        return True
    else:
        return False

print("[{}]:", match_brackets("[{}]"))
print("[{]}:", match_brackets("[{]}"))
print("[[{}]:", match_brackets("[[{}]"))
print("}{}[]:", match_brackets("}{}[]"))
