"""
https://dmoj.ca/problem/dmopc16c1p0
"""


def pizza_rater():
    """
    Read in statistics about a pizza and return its rating. Either `absolutely`,
    `fairly` or `very`.
    """
    width = int(input())
    chee_perc = int(input())

    if width == 3 and chee_perc >= 95:
        satis = "absolutely"
    elif width == 1 and chee_perc <= 50:
        satis = "fairly"
    else:
        satis = "very"

    print(f"C.C. is {satis} satisfied with her pizza.")


if __name__ == "__main__":
    pizza_rater()
