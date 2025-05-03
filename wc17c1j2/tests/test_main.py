"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import convert_fahr_to_cels


def test_convert_fahr_to_cels_exp01(capsys):
    with StringIO("20") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        convert_fahr_to_cels()
        captured = capsys.readouterr()
        assert "68\n" == captured.out
