from typing import List, Tuple


def find_summed_nums(nums: List[int], target: int) -> Tuple[int, int] | Tuple[()]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        else:
            seen[num] = i
    return ()

if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, (0, 1)), # basic case
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 25], 27, (6, 10)), # basic long case
        ([2, 3, 6, 12, 13], 15, (1, 3)), # basic case 2
        ([1, 2, 3, 4, 5, 6, 7], 5, (1, 2)), # multiple answer case
        ([0, 1, 2, 0, 3, 4], 0, (0, 3)), # zeros
        ([3, 3], 6, (0, 1)), # duplicate values
        ([-3, 4, 3, 90], 0, (0, 2)), # negatives
        ([1], 2, ()), # too short
        ([], 5, ()), # empty list
        ([1, 2, 3], 100, ()), # no solution
    ]

    for i, (nums, target, expected) in enumerate(tests, start=1):
        result = find_summed_nums(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status} | nums={nums} | target={target}, expected={expected}, got={result}")
