sample_input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"

sample_input = sample_input.split("\n")
print(sample_input)

def part_one(l):
    index = l.index("")
    range_lines = l[:index]
    ingredients = l[index+1:]

    num_fresh = 0
    for ing in ingredients:
        ing_value = int(ing)
        for r in range_lines:
            start, end = map(int, r.split("-"))
            if start <= ing_value <= end:
                num_fresh += 1
                break

    return num_fresh

inp = open("day-5/input.txt").read().splitlines()

print(part_one(inp))


def slow_part_two(l):
    index = l.index("")
    range_lines = l[:index]

    fresh_ingredients = []

    for r in range_lines:
        print(f"Processing range: {r}")
        start, end = map(int, r.split("-"))
        for i in range(start, end + 1):
            if i not in fresh_ingredients:
                fresh_ingredients.append(i)

    return len(fresh_ingredients)

def part_two(l):
    index = l.index("")
    range_lines = l[:index]

    fresh_ingredients = []



    for r in range_lines:
        start, end = map(int, r.split("-"))
        fresh_ingredients.append((start, end))

    fresh_ingredients.sort()

    # remove intervals with the same start
    cleaned_intervals = []
    for interval in fresh_ingredients:
        if not cleaned_intervals or interval[0] > cleaned_intervals[-1][1]:
            cleaned_intervals.append(interval)
        else:
            cleaned_intervals[-1] = (cleaned_intervals[-1][0], max(cleaned_intervals[-1][1], interval[1])) # merge interval by extending end if needed
    
    fresh_ingredients = cleaned_intervals

    # merge overlapping intervals
    merged_intervals = [fresh_ingredients[0]]

    for start,end in fresh_ingredients[1:]:
        last_interval = merged_intervals[-1]
        if start <= last_interval[1]:  # overlap
            merged_intervals[-1] = (last_interval[0], max(last_interval[1], end))  # merge
        else:
            merged_intervals.append((start, end))

    # sum the differences in the ranges
    total_fresh = 0
    for start, end in fresh_ingredients:
        total_fresh += end - start + 1
    
    print(fresh_ingredients)
    return total_fresh

print(part_two(inp))