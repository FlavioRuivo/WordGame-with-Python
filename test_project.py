import pytest

from project import high_score, my_score_help_half, translate


def test_translate():
    assert translate("PT", 1) == "Escolher Nivel: "
    assert translate("EN", 1) == "Choose Level: "


def test_high_score():
    assert high_score(10) == 45
    assert high_score(100) == 100


def test_my_score_help_half():
    assert my_score_help_half(10, 4) == 8
    assert my_score_help_half(20, 6) == 17
    assert my_score_help_half(24, 8) == 20
