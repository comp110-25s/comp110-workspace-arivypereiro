"""Using the dictionary function"""

__author__ = "730671996"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in my_dictionary:
        value = my_dictionary[key]
        if value in inverted:
            raise KeyError("error key duplicate")
        my_dictionary[value] = key
    return my_dictionary


def count(strs: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for s in strs:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts


def favorite_color(color_dictionary: dict[str, str]) -> str:
    favorites: dict[str, str] = {}
    for key in color_dictionary:
        color = color_dictionary[key]
        if color_dictionary[key] in favorites:
            number_of_favorite += 1
        else:
            number_of_favorite = 0
        return color_dictionary[key]


def bin_len(bin_list: list[str]) -> dict[int, set[str]]:
    bins = dict[int, set[str]] = {}
    for b in bin_list:
        if len(b) in bins:
            bins[len(b)] += 1
        else:
            bins[len(b)] = 1
    return bins
