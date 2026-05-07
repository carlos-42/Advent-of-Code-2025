# Day 1: Part 1 - counting the number of times the dial input goes to 0
sample_input = ["L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"]

inp = open("day-1/input.txt").read().strip().split("\n")

def count_zero_dials(dial_inputs):
    zero_count = 0
    dial_num = 50 # start at 50

    # Process each dial input
    # Dial are numbers from 0 to 99

    for dial in dial_inputs:
        direction = dial[0]
        value = int(dial[1:]) # can be any positive integer

        value = value % 100  # Normalize value to be within 0-99

        if direction == 'L':
            if value > dial_num:
                dial_num = 100 - (value - dial_num)
            else:
                dial_num -= value

        elif direction == 'R':
            if dial_num + value > 99:
                dial_num = (dial_num + value) - 100
            else:   
                dial_num += value

        if dial_num == 0:
            zero_count += 1
    return zero_count

result = count_zero_dials(inp)
print(f"Number of times the dial goes to 0: {result}")

def count_all_zero_dials(dial_inputs):
    zero_count = 0
    dial_num = 50 # start at 50

    # Process each dial input
    # Dial are numbers from 0 to 99

    for dial in dial_inputs:
        direction = dial[0]
        value = int(dial[1:]) # can be any positive integer


        hits_zero = value // 100 # Count how many times we pass 0 in full cycles
        zero_count += hits_zero

        value = value % 100  # Normalize value to be within 0-99
        
        if direction == 'L':
            if value > dial_num:
                zero_count -= 1 if dial_num == 0 else 0 # prevent double counting if we start at 0
                dial_num = 100 - (value - dial_num)
                zero_count += 1 if dial_num > 0 else 0
            else:
                dial_num -= value

        elif direction == 'R':
            if dial_num + value > 99:
                dial_num = (dial_num + value) - 100
                # only count passing zero if we actually cross it
                zero_count += 1 if dial_num > 0 else 0
            else:   
                dial_num += value

        if dial_num == 0:
            zero_count += 1  # Adjust for landing exactly on 0
    return zero_count

result_all = count_all_zero_dials(inp)
print(f"Total number of times the dial goes to 0 (including multiple times in one move): {result_all}")
