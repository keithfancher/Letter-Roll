#!/usr/bin/env python


import re


DICT = "american-english"
LETTERS = "ecp"
RE = r"[a-z]*e[a-z]*c[a-z]*p[a-z]*" # and all orderings of the letters... capital?


def main():
    d = open(DICT)
    for word in d:
        if re.search(RE, word) and "'" not in word:
            print word,
    d.close()


if __name__ == "__main__":
    main()
