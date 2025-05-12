"""
https://dmoj.ca/problem/ccc18j1
"""


def phone_filter():
    """
    Determine if the phonenumber should be answered or ignored.
    """
    digits = [int(input()) for _ in range(4)]

    if (
        (digits[0] == 8 or digits[0] == 9)
        and (digits[3] == 8 or digits[3] == 9)
        and (digits[1] == digits[2])
    ):
        print("ignore")
    else:
        print("answer")


if __name__ == "__main__":
    phone_filter()
