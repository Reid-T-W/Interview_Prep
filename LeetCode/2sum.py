#!/usr/bin/env python3
numbers = [2,7,11,15], target = 9


diff = target - numbers[0]
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for index, num in enumerate(numbers):
        diff = num[index] - target
        if diff < 0:
            diff = -1 * diff
        