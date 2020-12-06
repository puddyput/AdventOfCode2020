from adv_05.solve import SeatDecoder
import pytest


@pytest.mark.parametrize("input,expected", [
    ("FFFFFFFRRR", 7),
    ("FFFFFFFRLL", 4),
    ("FFFFFFFRLR", 5),
])
def test_parse_seat_rrr(input, expected):
    seat = SeatDecoder(input)
    assert seat.seat == expected

@pytest.mark.parametrize("input,expected", [
    ("BFFFBBFRRR", 70),
    ("FFFBBBFRRR", 14),
    ("BBFFBBFRLL", 102),
])
def test_parse_seat_rrr(input, expected):
    seat = SeatDecoder(input)
    assert seat.row == expected

