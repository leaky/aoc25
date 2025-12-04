def max_joltage(bank: str) -> int:
    """
    compute the highest possible two-digit number from a string of digits.

    this function interprets the input string as a sequence of single decimal digits,
    then evaluates all ordered pairs (i, j) with i < j to form two-digit numbers
    (digits[i] as the tens place and digits[j] as the ones place) it then returns the
    max two-digit number found.

    example:
        max_joltage("5027")  # evaluates pairs: 50, 52, 57, 02, 07, 27 -> returns 57
    """
    digits = [int(c) for c in bank.strip()]
    highest = 0
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            val = digits[i] * 10 + digits[j]
            if val > highest:
                highest = val
    return highest

def solve(filename: str) -> int:
    total = 0
    with open(filename) as f:
        for line in f:
            if line.strip():
                total += max_joltage(line)
    return total

if __name__ == "__main__":
    print(solve("data.txt"))