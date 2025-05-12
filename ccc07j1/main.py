"""
https://dmoj.ca/problem/ccc07j1
"""


def median_weight():
    """
    Find the calories of the supplied meal.
    """
    nums = [int(input()) for _ in range(3)]
    nums.sort()
    print(nums[1])


if __name__ == "__main__":
    median_weight()
