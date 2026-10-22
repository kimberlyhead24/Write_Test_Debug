import sys

def to_decimal(binary: str) -> int:
    result = 0
    for i, char in enumerate(reversed(binary)):
        if char not in "10":
            raise ValueError(f"Not a valid binary number: {char}")
        result += int(char) * (2**i)
    
    return result

if __name__ == "__main__":
    binary = sys.argv[1]
    print(to_decimal(binary))    