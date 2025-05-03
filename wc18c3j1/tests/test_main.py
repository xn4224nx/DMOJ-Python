"""
Tests for the main script.
"""

import sys
from io import StringIO
from main import pokemon_profit


def test_pokemon_profit_exp01(capsys):
    with StringIO("14\n3\n10") as prf:
        stdin = sys.stdin
        sys.stdin = prf
        pokemon_profit()
        captured = capsys.readouterr()
        assert "42\n" == captured.out
