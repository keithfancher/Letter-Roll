#!/usr/bin/env python


import argparse
import gzip
import itertools
import re


def get_reg_expressions(letters):
    """Generates a list of regular expressions for all the unique permutations
    of the given letters. These REs will then be matched against all the words
    in a given dictionary."""
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
    """Returns True if any of the regular expressions in the given list match
    the given word. Returns False otherwise."""
    for regexp in regexp_list:
        if re.search(regexp, word):
            return True
    return False


def get_matching_words(letters, dictionary):
    """Searches the given dictionary file for words that match the rolled
    letters. Returns words as a list."""
    matching_words = []

    for word in dictionary:
        reg_expressions = get_reg_expressions(letters)
        if word_matches_regexp_list(word, reg_expressions):
            # no contractions or proper nouns
            if "'" not in word and not word[0].isupper():
                matching_words.append(word.strip()) # strip whitespace

    return matching_words


def get_args():
    """Gets and parses command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-z', '--gunzip-dict', action='store_true', default=False,
                        help='gunzip the dictionary before searching')
    parser.add_argument('dict_file', action='store',
                        help='the dictionary to search through')
    parser.add_argument('letters', action='store',
                        help='the letters you rolled')
    return parser.parse_args()


def main():
    """My main() man!"""
    args = get_args()

    if args.gunzip_dict:
        dictionary = gzip.open(args.dict_file)
    else:
        dictionary = open(args.dict_file)

    matching_words = get_matching_words(args.letters, dictionary)
    for word in matching_words:
        print word

    dictionary.close()


if __name__ == "__main__":
    main()
