from typing import List


def minimum(values: List[int]) -> int:
    smallest_num = values[0]
    for number in values:
        if number < smallest_num:
            smallest_num = number
    return smallest_num


if __name__ == "__main__":
    print(minimum([3, 1, 4, 2]))        # expect 1
    print(minimum([5]))                 # expect 5
    print(minimum([-5, -1, -3]))        # expect -5
    print(minimum([0, -1, 10, -20]))    # expect -20

