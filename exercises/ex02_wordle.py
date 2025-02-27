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
    guess: str,
    secret: str,
    WHITE_BOX: str = "\U00002B1C",
    GREEN_BOX: str = "\U0001F7E9",
    YELLOW_BOX: str = "\U0001F7E8",
) -> str:
    """Test characters for colors"""
    assert len(guess) == len(secret)
    idx: int = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            return GREEN_BOX * len(guess)
        elif contains_char == True:
            return YELLOW_BOX * len(guess)
    return WHITE_BOX * len(guess)


def input_guess(N: int) -> str:
    print(f"Enter a 5 character word")
    guess_length: int = 5
    if N != guess_length:
        print(f"That wasn't {N} chars! Try again:")
