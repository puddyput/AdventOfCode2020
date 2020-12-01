from typing import List, Tuple


class FixReport:
    target: int
    data: List

    def __init__(self, target: int, data: List):
        self.target = target
        self.data = [int(s) for s in data]
        self.data.sort()

    def solve_two(self) -> int:
        indices = self._search(self.target, 0, len(self.data)-1)
        return self.data[indices[0]] * self.data[indices[1]]

    def solve_three(self) -> int:
        for i_third_leg in range(len(self.data)):
            v_third_leg = self.data[i_third_leg]
            if v_third_leg > self.target:
                continue

            indices = self._search(self.target-v_third_leg, 0, len(self.data)-1)
            if indices[0] == i_third_leg or indices[1] == i_third_leg:
                continue
            return v_third_leg * self.data[indices[0]] * self.data[indices[1]]

    def _search(self, target: int, i_low: int, i_high: int) -> Tuple[int, int]:
        v_low = self.data[i_low]
        v_high = self.data[i_high]
        _sum = v_low + v_high
        if _sum == target:
            return i_low, i_high
        if _sum > target:
            return self._search(target, i_low, i_high-1)
        return self._search(target, i_low+1, i_high)


with open("input.txt", "r") as file:
    finder = FixReport(2020, file.read().splitlines())
    print("solve for tuple: " + str(finder.solve_two()))
    print("solve for triple: " + str(finder.solve_three()))
