"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730691687"


import sys  # Import sys here so the exit function can be used in the input word and input letter defined functions


def input_word() -> str:
    word_input = input("Enter a 5-character word: ")
    if len(word_input) != 5:  # No else statement needed after to return the word put in
        print("Error: Word must contain 5 characters.")
        sys.exit()  # placed after error so that it can print that then exit the code
    return word_input


def input_letter() -> str:
    letter_input = input("Enter a single character: ")
    if len(letter_input) != 1:
        print("Error: Character must be a single character.")
        sys.exit()
    return letter_input


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    index: int = 0
    number_of_matches: int = 0
    while index < len(word):
        if word[index] == letter:
            print(
                str(letter) + " found at index " + str(index)
            )  # Print statement needs to repeat until all letters are found, change in condition stops message
            number_of_matches += 1
        index += 1
    if number_of_matches == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    elif number_of_matches == 1:
        print(
            str(number_of_matches)
            + " instance of "
            + str(letter)
            + " found in "
            + str(word)
        )
    else:
        print(
            str(number_of_matches)
            + " instances of "
            + str(letter)
            + " found in "
            + str(word)
        )


def main() -> None:
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


if __name__ == "__main__":
    main()
