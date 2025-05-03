"""
https://dmoj.ca/problem/dmopc14c5p1
"""

from math import pi


def cone_vol():
    """
    Calculate the volume of a cone.
    """
    radius = int(input())
    height = int(input())
    vol = pi * radius * radius * height / 3
    print(f"{vol:.2f}")


if __name__ == "__main__":
    cone_vol()
