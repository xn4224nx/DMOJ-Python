"""
https://dmoj.ca/problem/wc15c2j1
"""


def star_wars_distance():
    """
    Print the appropriate level of star wars distance.
    """
    num_fars = int(input()) - 1
    print("A long time ago in a galaxy far" + ", far" * num_fars + " away...")


if __name__ == "__main__":
    star_wars_distance()
