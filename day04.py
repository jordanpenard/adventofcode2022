

f = open("input_day04.txt", "r")
input_data = [x for x in f.read().split("\n") if x]

def create_range(a):
    x = a.split("-")
    start = int(x[0])
    end = int(x[1])+1
    return range(start, end)

list_of_ranges = [(create_range(x.split(",")[0]), create_range(x.split(",")[1])) for x in input_data]

def does_fully_overlapp(a, b):
    return set(a).issubset(set(b)) or set(b).issubset(set(a))

nb_of_full_overlapp = len(list(filter(lambda overlapp: overlapp == True, [does_fully_overlapp(a, b) for (a, b) in list_of_ranges])))

print("Part 1 : " + str(nb_of_full_overlapp))

def does_overlapp(a, b):
    return len(set(a).intersection(set(b))) >= 1

nb_of_overlapp = len(list(filter(lambda overlapp: overlapp == True, [does_overlapp(a, b) for (a, b) in list_of_ranges])))

print("Part 2 : " + str(nb_of_overlapp))
