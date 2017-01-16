#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open
import re
import sys

"""There are 2 files - file_with_text and file_dictionary
file_with_text have text with default delimiters(\s)
file_dictionary contains an arbitrary number of lines, each containing exactly one word.
"""


def update_text(searched_set, text_fname):
    """Create an html file with text in which every word that is searched updating

    :param searched_set: Set of searched words
    :param text_fname: File name of file with text for replace
    :return: returns nothing
    """
    with open(text_fname) as f, open('index.html', 'w', encoding='utf-8') as index:
        index.write(u'<html><head><meta charset="utf-8"/></head><body>\n')

        for line in f:
            replaced_line = ''

            for word in searched_set:
                replaced_line = re.sub(ur"[^а-яА-Я](" + word + ur")[^а-яА-Я]", update, line)
                # replaced_line = line.replace(word, update_func(word))

            index.write(replaced_line + '<br/>')

        index.write(u'\n</body></html>\n')


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


def update(matchobj):
    """Replace word with bolded html alternative"""
    line = matchobj.group(0)
    return line.replace(matchobj.group(1), u'<b>' + matchobj.group(1) + u'</b>')


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: dictionary_file text_file ')
        sys.exit(1)

    if not args[0] or not args[1]:
        print('usage: dictionary_file text_file ')
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
