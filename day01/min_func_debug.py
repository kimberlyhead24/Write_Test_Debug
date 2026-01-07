# Broken version used for Day 1 debugging practice.
# Bug: initializes smallest to 0, which breaks for all-positive lists.
def minimum(values):
    smallest = 0
    for i in range(1, len(values)):
        if values[i] < smallest:
            smallest = values[i]
    return smallest
