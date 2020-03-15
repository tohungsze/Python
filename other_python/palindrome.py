'''
    check if a given word is a palindrome
'''

def main():
    input = ['abcba', 'abc1cba', 'abcba ', 'abc1cba1']

    for word in input:
        if is_palindrome(word):
            print('\'%s\' is a palindrome'%word)
        else:
            print('\'%s\' is a NOT palindrome'%word)


def is_palindrome(input):  # takes a string as input (cannot take list)
    input_list = list(input)

    input_reverselist = input_list  # input_list and input_reverselist both points to same object

    input_reverselist.reverse()

    input_list = list(input)  # now input_list and input_reverselist point to different object

    result = True
    for i in range(len(input_list)):
        if input_list[i] == input_reverselist[i]:
            continue
        else:
            result = False
            break

    return result


if __name__ == '__main__':
    main()



