from collections import deque

def solve(path):
    dial = deque(range(100))

    with open(path) as f:
        instructions = f.read().splitlines()

    dial.rotate(-dial.index(50))

    count_zero = 0

    for line in instructions:
        direction = line[0]
        raw = "".join(ch for ch in line[1:] if ch.isdigit())
        steps = int(raw) if raw else 0

        if direction == "L":
            dial.rotate(steps)
        else:
            dial.rotate(-steps)

        if dial[0] == 0:
            count_zero += 1

    return count_zero

if __name__ == "__main__":
    result = solve("data.txt")
    print(result)