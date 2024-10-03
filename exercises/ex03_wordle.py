"""Exercise 3: Wordle"""

__author__ = "730691687"


def input_guess(secret_length: int) -> str:
    while True:
        guess = input(
            f"Enter a {secret_length} character word: "  # secret length will be 5 since secret is codes
        )  # f-string makes concat easier by just using {} to str argument, no more +
        if len(guess) == secret_length:
            return guess
        print(f"That wasn't {secret_length} chars! Try again: ")


def contains_char(word: str, single_char_input: str) -> bool:
    """"""
    assert (
        len(single_char_input) == 1
    )  # Assumption that character inputted is length of 1
    index = 0
    while index < len(
        word
    ):  # While loop with an index can cycle through word to see whether single character is found
        if word[index] == single_char_input:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Evaluates guessed inputs like how Wordle does"""
    assert len(guess) == len(secret)
    result = ""

    WHITE_BOX = "\U00002B1C"
    GREEN_BOX = "\U0001F7E9"
    YELLOW_BOX = "\U0001F7E8"

    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    # result += of any emoji builds the standard line of grey, green, or yellow boxes that evaluates whether letters are found in a word and in the right location
    # Can use already set variables as well, and does not need to add the codes for the emojis
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 6
    current_turn = 1
    won = False  # This allows for more turns to play out, until won is met

    while (
        current_turn <= turns and not won
    ):  # set loop condition where turns stay within 6 or less, and that won is not the bool set above
        print(f"=== Turn {current_turn}/{turns} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)  # Result is taken from emojify returned value

        if guess == secret:
            won = True
        current_turn += 1

    if won:
        print(
            f"You won in {current_turn - 1}/{turns} turns!"
        )  # Must account for extra loop that is gone through so current_turns is subtracted by 1
    else:
        print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
