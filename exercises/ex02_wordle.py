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


def emojified(guess_word: str, secret_word: str) -> str:
    """Test characters for colors"""
    assert len(guess_word) == len(
        secret_word
    ), "Guess must be the same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    full_word: str = ""
    while idx < len(guess_word):
        if guess_word[idx] == secret_word[idx]:
            full_word += GREEN_BOX
        elif contains_char(
            multiple_letter_word=secret_word, single_character=guess_word[idx]
        ):
            full_word += YELLOW_BOX
        else:
            full_word += WHITE_BOX
        idx += 1
    return full_word


def input_guess(N: int) -> str:
    guess = input(f"Enter a {N} character word:")
    while len(guess) != N:
        guess = input(f"That wasn't {N} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    current_turn: int = 1
    input_length: int = len(secret)
    while current_turn < 6:
        print(f"=== Turn{current_turn}/6 ===")
        guess_here = input_guess(N=input_length)
        print(emojified(secret_word=secret, guess_word=guess_here))
        current_turn += 1
        if secret == guess_here:
            return print(f"You won in {current_turn-1}/6 turns!")
    if secret != guess_here:
        return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
