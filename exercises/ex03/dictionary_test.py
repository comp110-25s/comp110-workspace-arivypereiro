__author__ = "730671996"

import pytest
from exercises.ex03.dictionary import invert


def key_error_invert_test() -> None:
    """Testing if values and keys invert correctly in dictionary."""
    with pytest.raises(KeyError):
        new_dictionary = {"x": "y", "w": "z"}
        invert(new_dictionary)


def inverting_correctly_test() -> None:
    new_dictionary = {"x": "y", "w": "z"}
    expected_dictionary = {"y": "x", "z": "w"}
    assert invert(new_dictionary) == expected_dictionary


def inverting_nothing_correctly_test() -> None:
    new_dictionary = {}
    expected_dictionary = {}
    assert invert(new_dictionary) == expected_dictionary
