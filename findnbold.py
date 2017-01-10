#!/usr/bin/python

import sys
import os
import re

"""There are 2 files - file_with_text and file_dictionary
file_with_text have text with default delimiters(\s)
file_dictionary contains an arbitrary number of lines, each containing exactly one word.
"""


def bold_word(word):
    """Replace word with bolded html alternative"""
    return "<b>" + word + "</b>"


def update_text(searched_dict, text_file):
    """Create an html file with text in which every word that in dictionary is bold

    :param searched_dict:
    :param text_file:
    :return:
    """
    index = file('index.html', 'w')
    index.write('<html><body>\n')

    f = open(text_file)

    for line in f:
        # Split every line in file to list and
        # replace each element which in searched_dict in bold
        replaced_line = (bold_word(el) if el in searched_dict else el for el in line.split(' '))

        # Trim list to line with space separation and add <br/> to the end
        index.write(' '.join(replaced_line) + "<br/>")

    index.write('\n</body></html>\n')
    index.close()


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: dictionary_file text_file '
        sys.exit(1)

    if not args[0] or not args[1]:
        print 'usage: dictionary_file text_file '
        sys.exit(1)

    dict_file = args[0]
    filename = args[1]

    searched_dict = set(word.strip() for word in open(dict_file))

    update_text(searched_dict, filename)


if __name__ == '__main__':
    main()
