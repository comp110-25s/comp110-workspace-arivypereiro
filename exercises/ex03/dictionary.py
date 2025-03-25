"""Using the dictionary function"""

__author__ = "730671996"


def invert(my_dictionary: dict[str, str]):
    inverted = {}
    for key in my_dictionary:
        value = my_dictionary[key]
        if value in inverted:
            raise KeyError("error key duplicate")
        my_dictionary[value] = key
    return my_dictionary
