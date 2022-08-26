#!/usr/bin/python3

def multiple_returns(sentence):

    if len(sentence) == 0:
        return None
    else:
        sent_len = len(sentence)
        first_str = sentence[0]
        return (sent_len, first_str)
