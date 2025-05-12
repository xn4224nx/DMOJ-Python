"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import meal_calories


def test_oldest_child_age_exp01(capsys):
    with StringIO("2\n1\n3\n4") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        meal_calories()
        captured = capsys.readouterr()
        assert "Your total Calorie count is 649.\n" == captured.out
