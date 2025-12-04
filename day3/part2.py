def max_joltage(bank: str) -> int:
    digits = [int(c) for c in bank.strip()]
    k = 12
    picked = []
    start = 0
    n = len(digits)

    # select k digits to form the largest number
    for _ in range(k):
        remaining = k - len(picked) # digits left to pick
        end = n - remaining + 1 
        best_digit = -1 # could be 0
        best_pos = start # position of the best digit

        # find the best digit in the range
        for i in range(start, end):
            if digits[i] > best_digit:
                best_digit = digits[i]
                best_pos = i

        picked.append(str(best_digit))
        start = best_pos + 1 # move start to the next position after the best digit
    
    # combine picked digits into the final number
    return int("".join(picked))

def solve(filename: str) -> int:
    total = 0
    with open(filename) as f:
        for line in f:
            if line.strip():
                total += max_joltage(line)
    return total

if __name__ == "__main__":
    print(solve("data.txt"))