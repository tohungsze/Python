#Given a string, find the length of the longest substring without repeating characters.
#Input: "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def no_repeat_char(input):
    charset = set()

    for c in input:
        if c not in charset:
            charset.add(c)
    if len(input) != len(charset):
        return False
    else:
        return True
    #test
    #print(no_repeat_char("abcd"))
    #print(no_repeat_char("aba"))



def longest_substring(input):
    substring = []
    for i in range(len(input)-1, -1, -1):   # trying from long to short
        # print("i=", i)                    # i is length of substring to try
                                            # i is the length of substring to try
        # print("i, j", i, i+1)
        for index in range(len(input)):     # index is the beginning of the substring
            if index + i <= len(input):     # making sure substring won't go beyond end of string
                substring = input[index:index+i]    # substring starting position j
                if no_repeat_char(substring):
                    print("Longest substring without repeat and length is:", substring, len(substring))
                    return

longest_substring("abcabcbb")   # expect 3
longest_substring("bbbbb")   # expect 1
longest_substring("pwwkew") # expect 3
