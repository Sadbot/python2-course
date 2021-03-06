#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""There are 2 files - file_with_text and file_dictionary
file_with_text have text with default delimiters(\s)
file_dictionary contains an arbitrary number of lines, each containing exactly one word.
"""

import re
import sys


def update_text(searched_set, text_fname):
    """Create an html file with text in which every word that is searched updating

    :param searched_set: Set of searched words
    :param text_fname: File name of file with text for replace
    :return: returns nothing
    """
    with open(text_fname) as text_file, open('index.html', 'w', encoding='utf-8') as index:
        index.write('<html><head><meta charset="utf-8"/></head><body>\n')

        for line in text_file:
            for word in searched_set:
                regex = re.compile(r'\b' + word + r'\b', re.U)
                line = regex.sub('<b>' + word + '</b>', line)
            index.write(line + '<br/>')

        index.write('\n</body></html>')


def read_set(dict_fname):
    """Open file with every line words and return set of this words

    :param dict_fname: File name with searched words
    :return: set() of searched words
    """
    searched_set = set()
    with open(dict_fname) as input_file:
        for line in input_file:
            searched_set.add(line.strip())
    return searched_set


def main():
    """Main function"""
    args = sys.argv[1:]

    if not args[0] or not args[1]:
        print('usage: dictionary_file text_file')
        sys.exit(1)

    dict_fname = args[0]
    text_fname = args[1]
    del args

    searched_set = read_set(dict_fname)
    if searched_set:
        update_text(searched_set, text_fname)
    else:
        print('No searched words')


if __name__ == '__main__':
    main()
