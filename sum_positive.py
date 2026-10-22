from typing import List
def sum_positive(values: List[int]) -> int:
    total_sum = 0
    for num in values:
        if num > 0:
            total_sum += num

    return total_sum

if __name__ == "__main__":
    print(sum_positive([]))        # expect 0
    print(sum_positive([5]))                 # expect 5
    print(sum_positive([-5, -1, -3]))        # expect 0
    print(sum_positive([0, -1, 10, -20]))    # expect 10
    print(sum_positive([10, 20, 5, 6, 8, 9])) # expect 58
