# to count all words starting with capital letter etc
# doesn't handle more than one most frequently used word - see last portion

import re
import operator

word_dict = {}
#most frequently used capitalized word
#with open("c://Temp/PythonCourse//DuplicateMax.txt", 'r') as f:
with open("c://Temp/PythonCourse//AliceInWonderland.txt", 'r') as f:
    for line in f.readlines():
        #line1 = re.sub(r'[^A-Za-z]', ' ', line)
        words = line.split()

        for word in words:
            if word.istitle():    # istitle() only works on single word, "Is it" will return False
                #print(word)
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

keymax = max(word_dict.items(), key=operator.itemgetter(1))[0]  # python3 with itemgetter
print('max frequency word starting with capital letter: [', str(keymax), "] used ", str(word_dict[keymax]), " times")

# most frequently used word
word_dict.clear()
with open("c://Temp/PythonCourse//AliceInWonderland.txt", 'r') as f2:
    for line in f2.readlines():
        line1 = re.sub(r'[^A-Za-z]', ' ', line)
        words = line.split()

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

keymax = max(word_dict.items(), key=operator.itemgetter(1))[0]  # python3 with itemgetter
print('max frequently used word: [', str(keymax), "] used ", str(word_dict[keymax]), " times")


# more than one most frequent word
word_dict.clear()
with open("c://Temp/PythonCourse//DuplicateMax.txt", 'r') as f:
    for line in f.readlines():
        # line1 = re.sub(r'[^A-Za-z]', ' ', line)
        words = line.split()

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

keymax = max(word_dict.items(), key=operator.itemgetter(1))[0]  # python3 with itemgetter

list1 = []

# handle case when more than one words share same max frequency
print(word_dict)
for key in word_dict:
    if word_dict[key] == word_dict[keymax]:
        list1.append(key)
print('max frequently used word3: used ', str(word_dict[keymax]), " times")
print('and the word(s) are:', list1)