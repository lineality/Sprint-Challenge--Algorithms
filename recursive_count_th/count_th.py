"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

# The base case is the exception:
# The base case is when there are no more letters in the word to check.
# Function: find the base case, and return the number of matches.
# Steps:
# 1. check for base case: if so, return number_of_matches
# otherwise:
# 2. call a checking helper-function
# - check the first two letters of a word
# - incriment countter if they match (th)
# - remove those letters from the word in any event
# - call the same function again on the remainder of the word


def count_th(word):

    # create variable to count matches
    number_of_matches = 0

    # word = "e" + word

    # testing inspection
    # print("main  word  is ", word)

    if len(word) == 0:
        pass

    # 1. check if number of remaining letters is zero (the base case)
    # a.k.a. check for base case: if so, return number_of_matches
    elif len(word) == 1:
        return number_of_matches

    # 2. otherwise, keep looking
    else:
        # counter += 1
        # print("counter", counter)
        word = word[1:]
        return check_again(word, count_th(word))


def check_again(word, number_of_matches):

    # this is the string being looked for
    string = "th"

    # testing inspection
    # print("helper word is ", word)

    # adjustint for case-insensitive search
    # word = word.lower()

    # checking to see if both letters are found in the input
    if word[0] == string[0] and word[1] == string[1]:
        number_of_matches += 1

    # returns only the number of matches
    return number_of_matches


# count_th("abcthefthghith")
