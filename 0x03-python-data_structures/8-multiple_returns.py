#!/usr/bin/python3

def multiple_returns(sentence):
    """ Returns a tuple with the length of a string and its first character """

    if len(sentence) == 0:
        return sentence[0] = None
    else:
        return (len(sentence), sentence[0])
