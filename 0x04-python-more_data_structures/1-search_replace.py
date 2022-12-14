#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == 2 else search for search in my_list]
