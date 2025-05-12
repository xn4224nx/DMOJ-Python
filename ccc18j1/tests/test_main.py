"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import phone_filter


def test_phone_filter_exp01(capsys):
    with StringIO("9\n6\n6\n8") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        phone_filter()
        captured = capsys.readouterr()
        assert "ignore\n" == captured.out


def test_phone_filter_exp02(capsys):
    with StringIO("5\n6\n6\n8") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        phone_filter()
        captured = capsys.readouterr()
        assert "answer\n" == captured.out


def test_phone_filter_exp03(capsys):
    with StringIO("8\n2\n2\n9") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        phone_filter()
        captured = capsys.readouterr()
        assert "ignore\n" == captured.out


def test_phone_filter_exp04(capsys):
    with StringIO("8\n3\n3\n8") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        phone_filter()
        captured = capsys.readouterr()
        assert "ignore\n" == captured.out


def test_phone_filter_exp05(capsys):
    with StringIO("9\n0\n0\n8") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        phone_filter()
        captured = capsys.readouterr()
        assert "ignore\n" == captured.out
