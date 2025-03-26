"""Using the dictionary function"""

__author__ = "730671996"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in my_dictionary:
        value = my_dictionary[key]
        if value in inverted:
            raise KeyError("error key duplicate")
        else:
            inverted[value] = key
    return inverted


def count(strs: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for s in strs:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts


def favorite_color(color_dictionary: dict[str, str]) -> str:
    favorites: dict[str, int] = {}
    color_frequency: str = ""
    for key in color_dictionary:
        color_frequency = color_dictionary[key]
        if color_frequency in favorites:
            favorites[color_frequency] += 1
        else:
            favorites[color_frequency] = 0
    color_count: int = 0
    color_name: str = ""
    for key in favorites:
        if color_count < favorites[key]:
            color_count = favorites[key]
            color_name = key
    return color_name


def bin_len(bin_list: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = {}
    for x in bin_list:
        if len(x) in bins:
            bins[len(x)].add(x)
        else:
            bins[len(x)] = {x}
    return bins
