from typing import List

def sum_positive(values: List[int]) -> int:
    total_sum = 0
    # BUGGY: starts from index 1 and skips the first element
    for i in range(0, len(values)):    # Changed the start of range to 0 from 1 
        if values[i] > 0:
            total_sum += values[i]
    return total_sum
