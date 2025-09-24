"""
CCC '02 J2 - AmeriCanadian
https://dmoj.ca/problem/ccc02j2
"""


def convert_words():
    """
    Convert the words between American English and Canadian English
    """
    vowels = ["a", "e", "i", "o", "u", "y"]

    while True:
        word = input().strip()

        if word == "quit!":
            break

        if len(word) > 4 and word[-2:] == "or" and word[-3] not in vowels:
            word = word[0:-2] + "our"

        print(word)


if __name__ == "__main__":
    convert_words()
