#!/usr/bin/python3

def multiple_returns(sentence):
    sent_len = len(sentence)

    if len(sentence) == 0:
        return (sent_len, None)
    else:
        first_str = sentence[0]
        return (sent_len, first_str)
