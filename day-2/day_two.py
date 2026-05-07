sample_input = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
"1698522-1698528","446443-446449","38593856-38593862","565653-565659",
"824824821-824824827","2121212118-2121212124"]

def sum_mirror_ids(ids):
    total = 0 

    for id in ids:
        start, end = id.split('-')
        for num in range(int(start), int(end) + 1):
            str_num = str(num)

            # look for mirror pattern
            length = len(str_num)
            mid = length // 2
            if length % 2 == 0:
                left = str_num[:mid]
                right = str_num[mid:]
                if left == right:
                    total += num
    return total

inp = open("day-2/input.txt").read().strip().split(",") # single line separated by commas
print(f"Sum of all invalid IDs on input: {sum_mirror_ids(inp)}")

def sum_invalid_ids(ids):
    total = 0 

    for id in ids:
        print("Searching ID range:", id)
        start, end = id.split('-')
        for num in range(int(start), int(end) + 1):
            str_num = str(num)

            # look for invalid pattern
            length = len(str_num)

            len_factors = []
            for i in range(1, length):
                if length % i == 0:
                    len_factors.append(i)

            is_invalid = False
            for factor in len_factors:
                segments = [str_num[j:j+factor] for j in range(0, length, factor)] # split into equal segments
                if all(segment == segments[0] for segment in segments):
                    is_invalid = True
                    print(f"Invalid ID found: {num}")
                    break
            if is_invalid:
                total += num
    return total
 
print(f"Sum of all invalid IDs on input: {sum_invalid_ids(inp)}")