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
        range = (0, self.columns_max)
        for c in seat_code:
            if c == "L":
                range = (range[0], (range[1] - math.ceil((range[1]-range[0]) / 2)))
            if c == "R":
                range = (math.ceil((range[0] + (range[1]-range[0]) / 2)), range[1])

        assert range[0] == range[1]
        self.seat = range[0]

    def _parse_row(self):
        row_code = self.row_matcher.findall(self.code)[0]
        range = (0, self.rows_max)
        for c in row_code:
            if c == "F":
                range = (range[0], (range[1] - math.ceil((range[1]-range[0]) / 2)))
            if c == "B":
                range = (math.ceil((range[0] + (range[1]-range[0]) / 2)), range[1])

        assert range[0] == range[1]
        self.row = range[0]


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
