"""Challenge Question 3: While loops"""

__author__ = "730691687"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
