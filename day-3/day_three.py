sample_input = ["987654321111111",
"811111111111119",
"234234234234278",
"818181911112111"]

def total_joltage(ratings):
    total = 0
    for r in ratings:
        print(r)
        # find largest number from index 0 to length - 1
        r_int = [int(i) for i in r]

        max_rating = max(r_int[:-1])
        # index of largest number
        index = r_int.index(max_rating)
        # find largest number from index to length
        second_max_rating = max(r_int[index+1:])


        jolts = str(max_rating) + str(second_max_rating) 
        print(f"jolts: {jolts}")
        total += int(jolts)
    return total

inp = open("day-3/input.txt").read().splitlines()
# print(total_joltage(inp))

def find_max(l, start, end):
    curr_max = -1
    idx = -1
    print(f"Finding max in {l[start:end]} from index {start} to {end}")
    for i in range(start, end+1):
        if l[i] > curr_max:
            curr_max = l[i]
            idx = i
    return curr_max, idx

def new_total_joltage(ratings):
    total = 0
    for r in ratings:
        # find largest 12 digit number in rating
        print(r)
        # find largest number from index 0 to index (length - 12) ... then next largest from there to (length -11) etc
        r_int = [int(i) for i in r]

        jolts = ""
        index = 0

        for i in range(0, 12):
            end = len(r_int) - 12 + i
            end = min(end, len(r_int))

            max_rating, index = find_max(r_int, index, end)
            jolts += str(max_rating)
            print(f"Jolts so far: {jolts}")
            # find inde
            index += 1 # needs to best exact index not the first index a value is found
            

        print(f"Final jolts: {jolts}")
        print(f"-------------------------------------------")
        total += int(jolts)

    return total



print(new_total_joltage(inp))