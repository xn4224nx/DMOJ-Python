"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import word_cnt


def test_word_cnt_exp01(capsys):
    with StringIO("problem one is really long") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        word_cnt()
        captured = capsys.readouterr()
        assert "5\n" == captured.out
