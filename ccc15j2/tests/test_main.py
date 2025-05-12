"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import message_sentiment


def test_exp01(capsys):
    with StringIO("How are you :-) doing :-( today :-)?") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        message_sentiment()
        captured = capsys.readouterr()
        assert "happy\n" == captured.out


def test_exp02(capsys):
    with StringIO(":)") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        message_sentiment()
        captured = capsys.readouterr()
        assert "none\n" == captured.out


def test_exp03(capsys):
    with StringIO("This :-(is str :-(:-a(nge te:-)xt.") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        message_sentiment()
        captured = capsys.readouterr()
        assert "sad\n" == captured.out
