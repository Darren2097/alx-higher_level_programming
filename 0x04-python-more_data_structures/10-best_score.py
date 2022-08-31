#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        score = None
        person = None

        for i in a_dictionary.keys():
            if score is None or a_dictionary[i] > score:
                score = a_dictionary[i]
                person = i

        return person
