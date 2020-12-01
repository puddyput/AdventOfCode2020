import pytest
from adv_01.fix_report import FixReport


def test_solve_first_basic_success():
    input = [1, 2, 2018, 2020]
    finder = FixReport(2020, input)
    assert finder.solve_two() == 2*2018
