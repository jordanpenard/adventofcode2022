import math
import re

def process(can_move_more_than_one_crate_at_a_time):
    f = open("input_day05.txt", "r")

    # split the data between stack drawing and operation list
    data = f.read().split("\n\n")
    stack = [x for x in data[0].split("\n") if x]
    operations = [x for x in data[1].split("\n") if x]

    # processing the stack of crate, ignoring the last line (with stack numbers) and starting from the bottom of the stack
    stack_hight = len(stack)-1
    nb_stacks = math.ceil(len(stack[stack_hight])/4)

    crate_collection = [[] for _ in range(nb_stacks)]

    for y in range(stack_hight-1, -1, -1):
        for x in range(0, nb_stacks):
            crate = stack[y][x*4+1]
            if crate != " ":
                crate_collection[x].append(crate)

    # processing the operations
    for operation in operations:

        result = re.search(r"move (\d+) from (\d+) to (\d+)", operation)
        nb_to_move = int(result.group(1))
        move_from = int(result.group(2))-1
        move_to = int(result.group(3))-1

        if (can_move_more_than_one_crate_at_a_time == False):
            for x in range(0, nb_to_move):
                crate_collection[move_to].append(crate_collection[move_from].pop())
        else:
            crate_collection[move_to].extend(crate_collection[move_from][-nb_to_move:])
            del crate_collection[move_from][-nb_to_move:]

    top_crates = [x[-1] for x in crate_collection]
    return "".join(top_crates)

print("Part 1 : " + process(False))
print("Part 2 : " + process(True))


