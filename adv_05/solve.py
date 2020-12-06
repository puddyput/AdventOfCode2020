import re
import math

class SeatDecoder:
    row: int
    seat: int
    rows_max = 127
    columns_max = 7
    code: str

    seat_matcher = re.compile(r"[LR]+")
    row_matcher = re.compile(r"[FB]+")

    def __init__(self, code: str):
        self.code = code
        self._parse_seat()
        self._parse_row()

    def _parse_seat(self):
        seat_code = self.seat_matcher.findall(self.code)[0]
        self.seat = self._close_in(self.columns_max, seat_code, "L", "R")

    def _parse_row(self):
        row_code = self.row_matcher.findall(self.code)[0]
        self.row = self._close_in(self.rows_max, row_code, "F", "B")

    def _close_in(self, max, code, use_lower, use_upper):
        range = (0, max)
        for c in code:
            if c == use_lower:
                range = (range[0], (range[1] - math.ceil((range[1] - range[0]) / 2)))
            if c == use_upper:
                range = (math.ceil((range[0] + (range[1] - range[0]) / 2)), range[1])

        assert range[0] == range[1]
        return range[0]


with open("input.txt") as file:
    highest = 0
    ids = []
    for line in file.readlines():
        seat = SeatDecoder(line)
        id = seat.row * 8 + seat.seat
        highest = max(highest, id)
        ids.append(id)

    print(highest)
    print([id+1 for id in ids if id+1 not in ids and id+2 in ids])
