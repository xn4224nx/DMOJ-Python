"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import basketball_game_result


def test_basketball_game_result_exp01(capsys):
    with StringIO("10\n3\n7\n8\n9\n6") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        basketball_game_result()
        captured = capsys.readouterr()
        assert "B\n" == captured.out


def test_basketball_game_result_exp02(capsys):
    with StringIO("7\n3\n0\n6\n4\n1") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        basketball_game_result()
        captured = capsys.readouterr()
        assert "T\n" == captured.out
