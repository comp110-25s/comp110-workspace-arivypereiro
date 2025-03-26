__author__ = "730671996"

import pytest
from dictionary import invert


def invert_test_error() -> None:
    """Testing for key error in dictionary."""
    with pytest.raises(KeyError):
        invert({"x": "y", "w": "y"})


def invert_test_two() -> None:
    """Testing if values and keys invert correctly in dictionary."""
    assert invert({"x": "y", "w": "z"}) == {"y": "x", "z": "w"}


def invert_test_empty() -> None:
    """Testing if empty dictionary inverts correctly."""
    assert invert({}) == {}


from dictionary import count


def test_count_key() -> None:
    """Testing if key is a unique value"""
    with pytest.raises(KeyError):
        count({"a", "a", "bb"})


from dictionary import favorite_color


def test_same_favorite_color() -> None:
    """Testing if key is favorite color"""
    assert favorite_color({"John": "blue", "Joseph": "blue", "Mary": "blue"}) == "blue"


def test_frequent_favorite_color() -> None:
    """Testing if key is favorite color"""
    assert (
        favorite_color(
            {"George": "yellow", "John": "green", "Joseph": "yellow", "Mary": "red"}
        )
        == "yellow"
    )


def test_tie_favorite_color() -> None:
    """Testing if key is favorite color"""
    assert (
        favorite_color(
            {"George": "red", "John": "purple", "Joseph": "purple", "Mary": "red"}
        )
        == "purple"
    )


from dictionary import bin_len


def test_bins_correctly() -> None:
    """Testing if it correctly bins"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bins_duplicates() -> None:
    """Testing if it correctly bins duuplicates"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
