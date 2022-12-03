#!/usr/bin/env python3
def remove_char_at(str, n):
    temp_str = ""
    i = 0;
    for c in str:
        if i == n:
            pass
        else:
            temp_str += c
        i += 1
    return temp_str
