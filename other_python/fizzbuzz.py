# a game to
# print 1 to 100
# print Fizz if a number is divisible by 3
# print Buzz if a number is divisible by 5
# print the number if a number is neither divisible by 3 nor 5

word_dict = {3:'Fizz', 5:'Buzz'}
#word_dict[3]='Fizz'
#word_dict[5]='Buzz'

#print (word_dict[5])

for i in range (1, 101):
    output = ''
    for x, y in word_dict.items():
        if i % x == 0:
            output += y
        #else:
        #    output = str(i)
        #print (i)
    if output == '':
        output = str(i)
    print(output)