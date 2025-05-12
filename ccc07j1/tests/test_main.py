"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import median_weight


def test_median_weight_exp01(capsys):
    with StringIO("10\n5\n8") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        median_weight()
        captured = capsys.readouterr()
        assert "8\n" == captured.out
