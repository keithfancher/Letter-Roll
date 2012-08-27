#!/usr/bin/env python


import itertools
import re
import sys


# filename of the dictionary to use (assumes one word per line)
DICT = "american-english"


def get_reg_expressions(letters):
    reg_expressions = []
    iterations = itertools.permutations(letters)

    # build the reg expressions
    for i in iterations:
        regexp = r"[a-z]*"
        for letter in i:
            regexp = regexp + letter + r"[a-z]*"
        reg_expressions.append(regexp)

    # Note that this can still result in duplicates, since permutations() uses
    # position to determine uniqueness. So if we rolled 'eep', the permutations
    # would be: eep, epe, eep, epe, pee, pee.
    #
    # In short, we need to remove dupes by hand:
    return list(set(reg_expressions))


def word_matches_regexp_list(word, regexp_list):
    for regexp in regexp_list:
        if re.search(regexp, word):
            return True
    return False


def main(argv):
    letters = argv[1]
    dictionary = open(DICT)

    # loop through all words in dictionary
    for word in dictionary:
        # loop through all possible reg expressions
        reg_expressions = get_reg_expressions(letters)
        if word_matches_regexp_list(word, reg_expressions):
            # no contractions or proper nouns
            if "'" not in word and not word[0].isupper():
                print word,

    dictionary.close()


if __name__ == "__main__":
    main(sys.argv)
