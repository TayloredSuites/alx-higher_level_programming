#!/usr/bin/python3

""" NO module importaton allowed
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters:
    ., ? and : (. ? :)
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    elif text[0] == " " or text[-1] == " ":
        text[0] = ""
        text[-1] = ""
    elif for i in text:
        if i == '.' or i == '?':
            print("\n\n")
            if i == ':':
                print("\n\n")

    return text
