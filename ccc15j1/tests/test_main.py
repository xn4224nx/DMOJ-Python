"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import special_day


def test_exp01(capsys):
    with StringIO("1\n7") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        special_day()
        captured = capsys.readouterr()
        assert "Before\n" == captured.out


def test_exp02(capsys):
    with StringIO("2\n18") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        special_day()
        captured = capsys.readouterr()
        assert "Special\n" == captured.out


def test_exp03(capsys):
    with StringIO("12\n1") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        special_day()
        captured = capsys.readouterr()
        assert "After\n" == captured.out


def test_exp04(capsys):
    with StringIO("2\n19") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        special_day()
        captured = capsys.readouterr()
        assert "After\n" == captured.out


def test_exp05(capsys):
    with StringIO("2\n17") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        special_day()
        captured = capsys.readouterr()
        assert "Before\n" == captured.out
