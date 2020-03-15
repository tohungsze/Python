'''
    check if a string has repeated characters
'''

def main():
    #print('in main')
    input = ['abcdef', 'abcabc', 'abc  def', 'Abcadef']

    for word in input:
        if hasrepeat(word):
            print('\'%s\' has repeated char' %word)
        else:
            print('\'%s\' does not have repeated char' %word)

def hasrepeat(input):
    input_list = input
    dict = {}

    result=False
    for i in range(len(input_list)):
        if input_list[i].lower() in dict:
            result = True
            break
        else:
            dict[input_list[i].lower()] = 1

    return result

if __name__ == "__main__":
    main()