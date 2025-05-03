"""
https://dmoj.ca/problem/wc18c3j1
"""


def pokemon_profit():
    """
    Determine the money that Team Roket can make from the resources they have
    available to them.
    """
    paint = int(input())
    paint_per_badge = int(input())
    badge_price = int(input())

    badges_made = paint // paint_per_badge
    leftover_paint = paint % paint_per_badge

    print(int(badges_made * badge_price + leftover_paint))


if __name__ == "__main__":
    pokemon_profit()
