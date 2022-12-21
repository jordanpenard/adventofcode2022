

f = open("input_day03.txt", "r")

input_data = [x for x in f.read().split("\n") if x]
input_data_split = [(x[0:int(len(x)/2)],x[int(len(x)/2):len(x)]) for x in input_data]

def find_duplicate(a, b):
    for i in a:
        if i in b:
            return i

duplicate_item_list = [find_duplicate(a, b) for (a, b) in input_data_split]

def get_priority(letter):
    if (letter.isupper()):
        return ord(letter)-65+27
    else:
        return ord(letter)-97+1

priority_list = list(map(get_priority, duplicate_item_list))

print("Part 1 : " + str(sum(priority_list)))

def find_badge(a, b, c):
    for i in a:
        if i in b and i in c:
            return i

badges = [find_badge(input_data[idx], input_data[idx+1], input_data[idx+2]) for idx in range(0, len(input_data), 3)]

badges_priority_list = list(map(get_priority, badges))

print("Part 2 : " + str(sum(badges_priority_list)))
