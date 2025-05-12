"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import ribbon_required


def test_ribbon_required_exp01(capsys):
    with StringIO("4 3\n0 2\n1 2\n3 4") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        ribbon_required()
        captured = capsys.readouterr()
        assert "1 3\n" == captured.out


def test_ribbon_required_exp02(capsys):
    with StringIO("20 4\n18 19\n4 16\n4 14\n5 12") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        ribbon_required()
        captured = capsys.readouterr()
        assert "7 13\n" == captured.out
