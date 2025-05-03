"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import visualise_spookiness


def test_word_cnt_exp01(capsys):
    with StringIO("5") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        visualise_spookiness()
        captured = capsys.readouterr()
        assert "spoooooky\n" == captured.out
