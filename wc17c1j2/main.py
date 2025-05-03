"""
https://dmoj.ca/problem/wc17c1j2
"""


def convert_fahr_to_cels():
    """
    Convert a temperature in degrees Celsius to Fahrenheit.
    """
    temp_cels = int(input())
    print(int((9 * temp_cels / 5) + 32))


if __name__ == "__main__":
    convert_fahr_to_cels()
