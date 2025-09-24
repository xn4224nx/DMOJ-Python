"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import convert_words


def test_exp01(capsys):
    with StringIO("color\nfor\ntaylor\nquit!\n") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        convert_words()
        captured = capsys.readouterr()
        assert "colour\nfor\ntaylour\n" == captured.out
