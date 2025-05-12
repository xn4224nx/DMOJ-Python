"""
https://dmoj.ca/problem/dmopc17c4p1
"""


def ribbon_required():
    """
    Read in ribbon data and determine the size of purple and blue ribbon
    required by the magical rabbit overlord.
    """
    first_line = [int(x) for x in input().split()]
    total_purple = first_line[0]
    num_paint_strokes = first_line[1]

    blu_strokes = [
        [int(x) for x in input().split(maxsplit=1)] for _ in range(num_paint_strokes)
    ]

    # Sort the list of paint strokes smallest to largest
    blu_strokes.sort()

    # Calculate the ammount of blue paint needed
    total_blue = 0
    furthest_right = 0
    for idx in range(len(blu_strokes)):
        if blu_strokes[idx][0] <= furthest_right:
            if blu_strokes[idx][1] > furthest_right:
                total_blue += blu_strokes[idx][1] - furthest_right
                furthest_right = blu_strokes[idx][1]

        else:
            total_blue += blu_strokes[idx][1] - blu_strokes[idx][0]
            furthest_right = blu_strokes[idx][1]

    # Show the result
    print(f"{total_purple-total_blue} {total_blue }")


if __name__ == "__main__":
    ribbon_required()
