#!/usr/bin/env python


import re
import itertools


DICT = "american-english"
LETTERS = "ecp"
RE = r"[a-z]*e[a-z]*c[a-z]*p[a-z]*" # and all orderings of the letters... capital?


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


def main():
    d = open(DICT)
    for word in d:
        if re.search(RE, word) and "'" not in word:
            print word,
    d.close()


if __name__ == "__main__":
    main()
