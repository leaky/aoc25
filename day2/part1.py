from bisect import bisect_left, bisect_right
from itertools import accumulate
from pathlib import Path


def generate_invalid_ids(limit: int) -> list[int]:
    """
        only numbers with an even digit count can be a repeated pattern
        (like: 2 digits, 4 digits, 6 digits, etc)
        
        for each even number of digits, the func determines how many digits are in the “half”
        eg: 4 digit numbers use a 2 digit repeating unit
        
        then:
            it loops over all possible first halves
            builds the full number by repeating that half twice
            stops early if the number exceeds the limit
            collects all valid numbers into a list and returns it
    """
    invalid: list[int] = []

    for length in range(2, len(str(limit)) + 1, 2):
        half = length // 2
        start = 10 ** (half - 1) # no leading zeros
        end = 10 ** half

        for root in range(start, end):
            num = int(str(root) * 2)
            if num > limit:
                break
            invalid.append(num)

    return invalid


def parse_ranges(line: str) -> list[tuple[int, int]]:
    """
        Parses a line of text containing ranges in the format "lo-hi,lo-hi,..."
        and returns a list of tuples representing those ranges.
    """
    parts = (p for p in line.strip().split(",") if p)
    return [tuple(map(int, part.split("-"))) for part in parts]


def sum_invalid_ids(path: str) -> int:
    """
        Reads ranges from a file, generates invalid IDs up to the maximum limit,
        and calculates the total count of invalid IDs within the specified ranges.

        bisect_left(invalid, lo) gives the index of the first invalid ID that is >= lo
		bisect_right(invalid, hi) gives the index just after the last invalid ID that is <= hi
    """
    data = Path(path).read_text(encoding="utf8").strip()
    ranges = parse_ranges(data)
    limit = max(hi for _, hi in ranges)

    invalid = sorted(generate_invalid_ids(limit))
    prefix = [0, *accumulate(invalid)]

    total = 0
    for lo, hi in ranges:
        left = bisect_left(invalid, lo)
        right = bisect_right(invalid, hi)
        total += prefix[right] - prefix[left]

    return total


if __name__ == "__main__":
    answer = sum_invalid_ids("data.txt")
    print(answer)