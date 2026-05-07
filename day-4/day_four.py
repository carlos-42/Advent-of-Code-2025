sample_input = ["..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."]

# print("\n".join(["".join(row) for row in sample_input]))

def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    accessible_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                # Check adjacent cells
                n = (r - 1, c)  # North
                s = (r + 1, c)  # South
                e = (r, c + 1)  # East
                w = (r, c - 1)  # West
                ne = (r - 1, c + 1)  # Northeast
                nw = (r - 1, c - 1)  # Northwest
                se = (r + 1, c + 1)  # Southeast
                sw = (r + 1, c - 1)  # Southwest

                roll_count = 0
                directions = [n, s, e, w, ne, nw, se, sw]
                for dr, dc in directions:
                    if 0 <= dr < rows and 0 <= dc < cols:
                        if grid[dr][dc] == "@":
                            roll_count += 1

                if roll_count < 4:
                    accessible_count += 1

    return accessible_count

inp = open("day-4/input.txt").read().splitlines()
print(count_accessible_rolls(inp))


def part_two(grid):
    rows = len(grid)
    cols = len(grid[0])

    accessible_count = 0
    can_continue = True


    while can_continue:
        run_count = 0
        positions_to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    # Check adjacent cells
                    n = (r - 1, c)  # North
                    s = (r + 1, c)  # South
                    e = (r, c + 1)  # East
                    w = (r, c - 1)  # West
                    ne = (r - 1, c + 1)  # Northeast
                    nw = (r - 1, c - 1)  # Northwest
                    se = (r + 1, c + 1)  # Southeast
                    sw = (r + 1, c - 1)  # Southwest

                    roll_count = 0
                    directions = [n, s, e, w, ne, nw, se, sw]
                    for dr, dc in directions:
                        if 0 <= dr < rows and 0 <= dc < cols:
                            if grid[dr][dc] == "@":
                                roll_count += 1

                    # remove this position if roll_count < 4
                    if roll_count < 4:
                        run_count += 1
                        accessible_count += 1
                        positions_to_remove.append((r, c))

        can_continue = run_count > 0

        for r, c in positions_to_remove:
            grid[r] = grid[r][:c] + "x" + grid[r][c+1:]
    return accessible_count

print(part_two(inp))