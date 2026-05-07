sample_input = '123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  '

sample_input = sample_input.split("\n")
sample_input = [line.strip().split() for line in sample_input]
print(sample_input)

def sum_problems(l):
    ops = l[-1]

    grand_total = 0
    for i in range(len(ops)):
        total = 0
        op = ops[i]
        numbers = []
        for list_item in l[:-1]:
            numbers.append(int(list_item[i]))
        
        if op == "+":
            total = sum(numbers)
        elif op == "*":
            total = 1
            for num in numbers:
                total *= num
        grand_total += total
    return grand_total

inp = open("day-6/input.txt").read().splitlines()
inp = [line.strip().split() for line in inp]
# print(inp)
# print(sum_problems(inp))

# part two
sample_input = '123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  '
sample_input = sample_input.split("\n")
sample_input = [line.split(" ") for line in sample_input]
print(sample_input)

# store the number of spaces between operators

inp = open("day-6/input.txt").read().splitlines()
inp = [line.split(" ") for line in inp]
ops = sample_input[-1]


operators = ['+', '*']
index = 0

indices = []
while index < len(ops):
    if ops[index] in operators:
        indices.append(index)
    index += 1


digits = []
for i in range(len(indices)):
    if i != len(indices) - 1:
        digits.append(indices[i+1] - indices[i])
    else:
        digits.append(len(ops) - indices[i])

print(digits)  # number of spaces between operators

sample_input = '123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  '
sample_input = sample_input.split("\n")

intervals = [(0, digits[0])]
for d in digits[1:]:
    start = intervals[-1][1]
    end = start + d
    intervals.append((start, end))

print(intervals)

lines = []
for line in sample_input[:-1]:
    numbers = []
    for interval in intervals:
        start, end = interval
        nums = line[start:end]
        numbers.append(nums)
    lines.append(numbers)

print(lines)

for i in range(len(ops)):
    total = 0
    op = ops[i]
    col_nums = []
    for j in range(digits[i]):
        col_num = []