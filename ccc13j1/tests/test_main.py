"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import oldest_child_age


def test_oldest_child_age_exp01(capsys):
    with StringIO("12\n15") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        oldest_child_age()
        captured = capsys.readouterr()
        assert "18\n" == captured.out


def test_oldest_child_age_exp02(capsys):
    with StringIO("10\n10") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        oldest_child_age()
        captured = capsys.readouterr()
        assert "10\n" == captured.out
