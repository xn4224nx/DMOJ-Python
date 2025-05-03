"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import star_wars_distance


def test_star_wars_distance_exp01(capsys):
    with StringIO("1") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        star_wars_distance()
        captured = capsys.readouterr()
        assert "A long time ago in a galaxy far away...\n" == captured.out


def test_star_wars_distance_exp02(capsys):
    with StringIO("2") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        star_wars_distance()
        captured = capsys.readouterr()
        assert "A long time ago in a galaxy far, far away...\n" == captured.out


def test_star_wars_distance_exp03(capsys):
    with StringIO("4") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        star_wars_distance()
        captured = capsys.readouterr()
        assert (
            "A long time ago in a galaxy far, far, far, far away...\n" == captured.out
        )
