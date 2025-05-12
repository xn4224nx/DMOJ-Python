"""
https://dmoj.ca/problem/dmopc14c5p1
"""


def special_day():
    """
    Determine if the supplied day is special.
    """
    special_day = (2, 18)
    month = int(input())
    day = int(input())

    if (month, day) < special_day:
        print("Before")

    elif (month, day) > special_day:
        print("After")

    else:
        print("Special")


if __name__ == "__main__":
    special_day()
