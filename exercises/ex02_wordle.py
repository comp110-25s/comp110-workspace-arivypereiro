"""Exercise for creating Wordle"""

__author__: str = "730671996"


def contains_char(multiple_letter_word: str, single_character: str) -> bool:
    """Search if it contains character based on parameters"""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    idx: int = 0
    while idx < len(multiple_letter_word):
        if multiple_letter_word[idx] == single_character:
            return True
        else:
            idx = idx + 1
    return False


def emojified(
    guess_word: str,
    secret_word: str,
    WHITE_BOX: str = "\U00002B1C",
    GREEN_BOX: str = "\U0001F7E9",
    YELLOW_BOX: str = "\U0001F7E8",
) -> str:
    """Test characters for colors"""
    assert len(guess_word) == len(secret_word)
    idx: int = 0
    if guess_word[idx] == secret_word [idx]:
        return GREEN_BOX
    elif contains_char == True
        return YELLOW_BOX
    return WHITE_BOX


def input_guess(N: int) -> str:
    guess = input(f"Enter a {N} character word:")
    while len(guess) != N:
        guess = input(f"That wasn't {N} chars! Try again:")
    return guess
