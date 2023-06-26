#!/usr/bin/python3
def best_score(a_dictionary):
    mx_score, mx_key = 0, 0
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    for key, score in a_dictionary.items():
        if score > mx_score:
            mx_score = score
            mx_key = key
    return mx_key
