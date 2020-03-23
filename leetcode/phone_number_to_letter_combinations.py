"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

import logging

logging.basicConfig(level=logging.INFO)

letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def lettercombinations(digits: str):
    if len(digits) == 0:  # really gonna pass an empty string :|
        return "Empty input"
    if "0" in digits or "1" in digits:
        return "invalid entry"

    result = [""]
    for d in digits:
        tmp = []
        while len(result) > 0:  # make a copy of result and then clear it
            tmp.append(result.pop())

        for ch in letters[d]:
            logging.debug("ch=", ch)
            for partial in tmp:
                logging.debug("partial=", partial)
                result.append(partial + ch)
            logging.debug("result=", result)
    return result


print(lettercombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
