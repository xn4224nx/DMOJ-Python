"""
https://dmoj.ca/problem/dmopc14c5p1
"""


def oldest_child_age():
    """
    Find the age of the oldest child.
    """
    age_0 = int(input())
    age_1 = int(input())
    print(2 * age_1 - age_0)


if __name__ == "__main__":
    oldest_child_age()
