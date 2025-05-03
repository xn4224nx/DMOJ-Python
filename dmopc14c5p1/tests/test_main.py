"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import cone_vol


def test_cone_vol_exp01(capsys):
    with StringIO("3\n5") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        cone_vol()
        captured = capsys.readouterr()
        assert "47.12\n" == captured.out
