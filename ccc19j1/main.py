"""
https://dmoj.ca/problem/ccc19j1
"""


def basketball_game_result():
    """
    Read the teasm statistics and determine what the game result is. A means the
    first team one, B means the second did and T means it is a tie.
    """
    data = [int(input()) for _ in range(6)]
    team0_scr = data[0] * 3 + data[1] * 2 + data[2]
    team1_scr = data[3] * 3 + data[4] * 2 + data[5]

    if team0_scr > team1_scr:
        print("A")
    elif team0_scr < team1_scr:
        print("B")
    else:
        print("T")


if __name__ == "__main__":
    basketball_game_result()
