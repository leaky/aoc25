from collections import deque

def solve(path):
    with open(path) as f:
        instructions = f.read().splitlines()

    count_zero = 0
    cur = 50 

    for line in instructions:
        if not line:
            continue

        direction = line[0]
        try:
            steps = int(line[1:])
        except ValueError:
            continue

        step_sign = -1 if direction == "L" else 1

        for _ in range(steps):
            cur = (cur + step_sign) % 100
            if cur == 0:
                count_zero += 1

    return count_zero

if __name__ == "__main__":
    result = solve("data.txt")
    print(result)