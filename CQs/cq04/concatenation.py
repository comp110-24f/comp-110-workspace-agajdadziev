"""Challenge Question 4.1 Concatenation"""

__author__ = "730691687"


def concat(string1: str, string2: str) -> str:
    return string1 + string2


word1 = "happy"
word2 = "tuesday"
print(concat(word1, word2))
if __name__ == "__main__":
    result = concat(word1, word2)
    print(result)
