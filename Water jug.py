from collections import deque

def water_jug(capA, capB, target):
    visited = set()
    queue = deque()

    queue.append((0, 0))      # initial state
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        print(f"Current State: ({x}, {y})")

        if x == target or y == target:
            print("Target achieved!")
            return

        states = [
            (capA, y),                 # Fill Jug A
            (x, capB),                 # Fill Jug B
            (0, y),                    # Empty Jug A
            (x, 0),                    # Empty Jug B
            (min(capA, x + y), max(0, x + y - capA)),  # Pour B → A
            (max(0, x + y - capB), min(capB, x + y))   # Pour A → B
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)


# -------- INPUT --------
jugA = 4
jugB = 3
target = 1

water_jug(jugA, jugB, target)
