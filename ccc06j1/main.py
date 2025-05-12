"""
https://dmoj.ca/problem/ccc06j1
"""


def meal_calories():
    """
    Find the calories of the supplied meal.
    """
    cals = [
        [461, 431, 420, 0],
        [130, 160, 118, 0],
        [100, 57, 70, 0],
        [167, 266, 75, 0],
    ]

    # Get the user inputs as the index in the calorie vector
    burger_num = int(input()) - 1
    side_num = int(input()) - 1
    drink_num = int(input()) - 1
    deser_num = int(input()) - 1

    # Count the calories
    calories = (
        cals[0][burger_num]
        + cals[1][drink_num]
        + cals[2][side_num]
        + cals[3][deser_num]
    )
    print(f"Your total Calorie count is {calories}.")


if __name__ == "__main__":
    meal_calories()
