from bisect import bisect_left, bisect_right
from itertools import accumulate
from pathlib import Path

def generate_invalid_ids(limit: int) -> list[int]:
    """
    return all numbers <= limit that with a digit block repeated twice or more.

    a valid number has:
        - a block with no leading zero
        - at least two repetitions
        - total length and value not exceeding the limit

    the function:
        tries every possible block length
        builds all digit blocks of that length (no leading zero)
        repeats each block (block * reps) for reps >= 2. 
    
    (repetition stops when the resulting number becomes longer than the limit allows or exceeds the numeric limit.)
    """
    invalid: list[int] = []
    max_len = len(str(limit))

    for block_len in range(1, max_len // 2 + 1):
        start = 10 ** (block_len - 1)
        end = 10 ** block_len

        for root in range(start, end):
            block = str(root)
            reps = 2

            while True:
                num_s = block * reps
                if len(num_s) > max_len:
                    break

                num = int(num_s)
                if num > limit:
                    break

                invalid.append(num)
                reps += 1

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

    invalid = sorted(set(generate_invalid_ids(limit)))
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