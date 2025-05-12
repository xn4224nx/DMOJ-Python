"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import pizza_rater


def test_pizza_rater_exp01(capsys):
    with StringIO("2\n70") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        pizza_rater()
        captured = capsys.readouterr()
        assert "C.C. is very satisfied with her pizza.\n" == captured.out
